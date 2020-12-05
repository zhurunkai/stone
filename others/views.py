from django.shortcuts import render, HttpResponse
from login_signup.models import Users
from posts.models import Posts
from backmanage.models import Feedback
import json
# Create your views here.


def about(request):
    return render(request, 'about.html')


def write_advice(request):
    return render(request, 'complain.html')


def media(request):
    return render(request, 'media.html')


def newmain(request):
    return render(request, 'newmain.html')


def user1(request):
    phone_number = request.session.get('phone_number')
    user_info = Users.objects.get(phone_number=phone_number)
    user_info.posts = json.loads(user_info.posts)
    user_info.joinposts = json.loads(user_info.joinposts)
    postin = []
    for post in user_info.posts:
        postabc = Posts.objects.get(id=post)
        postin.append(postabc)
    return render(request, 'user.html', {'user_info': user_info, 'post_info': postin})
    # print(postin)
    # return HttpResponse(1)


def user2(request):
    phone_number = request.session.get('phone_number')
    user_info = Users.objects.get(phone_number=phone_number)
    user_info.posts = json.loads(user_info.posts)
    user_info.joinposts = json.loads(user_info.joinposts)
    return render(request, 'user2.html', {'user_info': user_info})


def stone(request):
    return render(request, 'stone.html')


def main_part(request):
    return render(request, 'main_part.html')