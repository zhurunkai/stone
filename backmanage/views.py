from django.shortcuts import render, HttpResponse, redirect, reverse
from login_signup.models import Users
from posts.models import Posts
from home.models import Record
from django.http import HttpResponseRedirect
import time
import json
from .models import Feedback
import os
import os
from django import forms
import psutil

# Create your views here.


# 封装md5加密函数
def md5(strr):
    import hashlib
    m = hashlib.md5()
    m.update(strr.encode("utf8"))
    return m.hexdigest()


# 登录检测
def auth(request):
    if not request.session.get('phone_number'):
        return redirect('login_signup:login_page')


def index(request):
    if not request.session.get('phone_number'):
        return redirect('login_signup:login_page')
    admins = Users.objects.filter(auth=1)
    users = Users.objects.filter(auth=0)
    return render(request, 'manage.html', {'users': users, 'admins': admins})


def feedback(request):
    advices = Feedback.objects.all()

    return render(request, 'feedback.html', {'advices': advices})


def forum_task(request):
    res = Posts.objects.all()
    for individual in res:
        individual.keywords = json.loads(individual.keywords)
        individual.comments = json.loads(individual.comments)
    return render(request, 'forum-task.html', {'posts': res})


def system_state(request):
    return render(request, 'system-state.html')


def user_manage(request):
    users = Users.objects.all()
    for user in users:
        user.posts = json.loads(user.posts)
        user.posts_num = len(user.posts)
    users_num = len(users)
    posts_num = len(Posts.objects.all())
    date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))[:10]
    if Record.objects.filter(datetime=date):
        resu = Record.objects.get(datetime=date)
        res = resu.num
    else:
        Record.objects.create(datetime=date, num=0)
        res = 0
    return render(request, 'user-manage.html', {'users': users, 'users_num': users_num,
                                                'posts_num': posts_num, 'skin': res})


# 获取内存、CPU、网络、硬盘使用状况
# def seek_selfinfo(request):

# 设为管理
def set_admin(request, user_id):
    user_info = Users.objects.get(id=user_id)
    user_info.auth = 1
    user_info.save()
    return redirect('backmanage:user_manage')


# 解除管理
def remove_admin(request, user_id):
    user_info = Users.objects.get(id=user_id)
    user_info.auth = 0
    user_info.save()
    return redirect('backmanage:user_manage')


# 屏蔽用户
def forbid_user(request, user_id):
    user_info = Users.objects.get(id=user_id)
    if user_info.forbid == 1:
        user_info.forbid = 0
    else:
        user_info.forbid = 1
    user_info.save()
    return redirect('backmanage:user_manage')


# 重置密码
def reset_password(request, user_id):
    user_info = Users.objects.get(id=user_id)
    user_info.password = md5('12345')
    user_info.save()
    return redirect('backmanage:user_manage')


# 删除帖子
def remove_post(request, post_id):
    post_info = Posts.objects.get(id=post_id)
    author = post_info.author
    join_data = json.loads(post_info.comments)
    join_users = []
    for join in join_data:
        join_users.append(join['uid'])
    author_info = Users.objects.get(id=author)
    author_info.posts = json.loads(author_info.posts)
    for c in author_info.posts:
        if c == int(post_id):
            author_info.posts.remove(c)
    author_info.posts = json.dumps(author_info.posts, ensure_ascii=False)
    author_info.save()
    for join_user in join_users:
        user_info = Users.objects.get(id=join_user)
        user_info.joinposts = json.loads(user_info.joinposts)
        for a in user_info.joinposts:
            if a == post_id:
                user_info.joinposts.remove(a)
        user_info.joinposts = json.dumps(user_info.joinposts, ensure_ascii=False)
        user_info.save()
    Posts.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('backmanage:forum_task'))


def about(request):
    return render(request, 'about.html')


def star(request, feedback_id):
    feedback_info = Feedback.objects.get(id=feedback_id)
    if feedback_info.star == 0:
        feedback_info.star = 1
    else:
        feedback_info.star = 0
    feedback_info.save()
    return redirect('backmanage:feedback')


# 审核通过
def pass_post(request, post_id):
    post_info = Posts.objects.get(id=post_id)
    post_info.resolved = 1
    post_info.save()
    return redirect('backmanage:forum_task')


# 审核不通过
def fail_post(request, post_id):
    post_info = Posts.objects.get(id=post_id)
    post_info.resolved = -1
    post_info.save()
    return redirect('backmanage:forum_task')


def advise(request):
    content = request.POST.get('content')
    datetime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    if request.FILES.get('annex'):
        annex = request.FILES.get('annex')
        timest = str(time.time())[:-8]
        file_path = 'backmanage/static/upload/' + timest + annex.name
        f = open(file_path, 'wb')
        for chunk in annex.chunks():
            f.write(chunk)
        f.close()
        Feedback.objects.create(content=content, star=0, time=datetime, annex='/static/upload/' + timest + annex.name)
    else:
        Feedback.objects.create(content=content, star=0, time=datetime, annex='')
    return redirect('home:index')
