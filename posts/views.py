from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Posts
from login_signup.models import Users
import json
import time
# Create your views here.


# 登录检测
def auth(request):
    if not request.session.get('phone_number'):
        return redirect('login_signup:login_page')


# 检测session获取用户数据
def user_seek(request):
    if request.session.get('phone_number'):
        user_info = Users.objects.get(phone_number=request.session.get('phone_number'))
        return user_info
    else:
        return 0


# 获取贡献榜数据
def contribution_seek(request):
    contribution_data = Users.objects.all().order_by('-contribution')
    condata = contribution_data[:5]
    return condata


# 列表显示
def list_page(request, page):
    res = Posts.objects.all().order_by("-id")
    user_info = user_seek(request)
    contribution_data = contribution_seek(request)
    for question in res:
        question.keywords = json.loads(question.keywords)
        question.comments = json.loads(question.comments)
        question.comment_len = len(question.comments)
    allpage = len(res) // 4 + 1
    if page == allpage:
        ress = res[4*(page-1):]
    else:
        ress = res[4*(page-1):4*page]
    # pagelen = range(7)
    pagelen = []
    for i in range(allpage):
        pagelen.append(i+1)
    lenth = len(pagelen)
    return render(request, 'list_page.html', {'lists': ress, 'user_info': user_info,
                                              'contribution': contribution_data,
                                              'page': page, 'pagelen': pagelen,
                                              'lowpage': page-1, 'hignpage': page+1,
                                              'lenth': lenth})


# 帖子显示
def content_page(request, post_id):
    post_res = Posts.objects.get(pk=post_id)
    post_res.comments = json.loads(post_res.comments)
    post_res.comment_len = int(len(post_res.comments))
    post_res.keywords = json.loads(post_res.keywords)
    new_volume = post_res.volume + 1
    revise = Posts.objects.get(pk=post_id)
    revise.volume = new_volume
    revise.save()
    user_info = user_seek(request)
    con = contribution_seek(request)
    return render(request, 'content_page.html', {'post': post_res, 'user_info': user_info,
                                                 'contribution': con})


# 发布帖子
def release(request):
    auth(request)
    phone_number = request.session.get('phone_number')
    user_info = user_seek(request)
    title = request.POST.get('title')
    content = request.POST.get('content')
    keywords = request.POST.get('keywords')
    time_obj = time.localtime(time.time())
    datetime = time.strftime("%Y/%m/%d %H:%M:%S", time_obj)
    keywords.replace(' ', '')
    new_keywords = keywords.split('#')
    new_keywords = new_keywords[1:]
    str_keywords = json.dumps(new_keywords, ensure_ascii=False)
    res = Posts.objects.create(title=title, content=content, time=datetime, author=user_info.id, thumbs=0,
                               comments='[]', keywords=str_keywords, volume=0, nickname=user_info.nickname,
                               head=user_info.head, resolved=0)
    revise = Users.objects.get(phone_number=phone_number)
    revise.posts = json.loads(revise.posts)
    revise.posts.append(int(res.id))
    revise.posts = json.dumps(revise.posts, ensure_ascii=False)
    revise.contribution += 123
    revise.save()
    return redirect(reverse('posts:list', kwargs={'page': 1}))


# 多字段模糊查询搜索
def search(request):
    user_info = user_seek(request)
    keywords = str(request.GET.get('keywords'))
    keys = keywords.split()
    res = []
    for key in keys:
        res1 = Posts.objects.filter(title__icontains=key)
        res2 = Posts.objects.filter(nickname__icontains=key)
        res3 = Posts.objects.filter(content__icontains=key)
        res4 = Posts.objects.filter(comments__icontains=key)
        res5 = Posts.objects.filter(keywords__icontains=key)
        all_res = list(res1) + list(res2) + list(res3) + list(res4) + list(res5)
        res += all_res
    res = list(set(res))
    for ind in res:
        ind.comments = json.loads(ind.comments)
        ind.keywords = json.loads(ind.keywords)
    # res = sorted(res, key=lambda x: x["volume"])
    # for individual in res:
    #     individual.keywords = json.loads(individual.keywords)
    #     individual.comments = json.loads(individual.comments)
    con = contribution_seek(request)
    return render(request, 'search_page.html', {'search_list': res, 'user_info': user_info,
                                                'keywords': keywords, 'contribution': con})


# 评论
def follow(request, post_id):
    auth(request)
    user_info = user_seek(request)
    content = request.POST.get('content')
    post_info = Posts.objects.get(id=post_id)
    post_info.comments = json.loads(post_info.comments)
    time_obj = time.localtime(time.time())
    datetime = time.strftime("%Y/%m/%d %H:%M:%S", time_obj)
    lenth = len(post_info.comments)
    post_info.comments.append({"id": lenth, "time": datetime, "uid": user_info.id, "nickname": user_info.nickname,
                               "head": user_info.head, "content": content})
    post_info.comments = json.dumps(post_info.comments, ensure_ascii=False)
    post_info.save()
    new_post = Posts.objects.get(id=post_id)
    new_post.comments = json.loads(new_post.comments)
    new_post.keywords = json.loads(new_post.keywords)
    new_user = Users.objects.get(id=user_info.id)
    new_user.joinposts = json.loads(new_user.joinposts)
    if post_id not in new_user.joinposts:
        new_user.joinposts.append(post_id)
    new_user.joinposts = json.dumps(new_user.joinposts, ensure_ascii=False)
    new_user.contribution += 74
    new_user.save()
    return redirect(reverse('posts:content', kwargs={"post_id": post_id}))





