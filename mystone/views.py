from django.shortcuts import render, HttpResponse, redirect
import time
from login_signup.models import Users
from .models import Mystone
import json
# Create your views here.


def indexmystone(request):
    return render(request, 'chooseMap.html')


def newindex(request):
    return render(request, 'index.html', {'state': 1})



def savegame(request):
    # if request.session.get('phone_number'):
    #     phone_number = request.session.get('phone_number')
    #     user_info = Users.objects.get(phone_number=phone_number)
    #     uid = user_info.id
    # else:
    #     return redirect('login_signup:login_page')
    # content = request.body
    # file_path = 'mystone/static/files/'+str(time.time())[:-8]+':a'+str(uid)+'.txt'
    # f = open(file_path, 'wb')
    # f.write(content)
    # f.close()
    # mystone = Mystone.objects.filter(uid=uid)
    # if len(mystone) == 0 :
    #     Mystone.objects.create(uid=uid, f=json.dumps([file_path], ensure_ascii=False))
    # else:
    #
    return HttpResponse(1)


def savedata(request):
    if request.session.get('phone_number'):
        phone_number = request.session.get('phone_number')
        user_info = Users.objects.get(phone_number=phone_number)
        uid = user_info.id
    else:
        return redirect('login_signup:login_page')

    content = request.body
    f = open('mystone/static/files/'+str(time.time())[:-8]+':b'+str(uid)+'.txt', 'wb')
    f.write(content)
    f.close()
    return HttpResponse(2)