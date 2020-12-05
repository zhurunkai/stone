from django.shortcuts import render, HttpResponse
import time
from login_signup.models import Users
from .models import Record
# Create your views here.


def index(request):
    datetime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    if Record.objects.filter(datetime=datetime[:10]):
        res = Record.objects.get(datetime=datetime[:10])
        res.num += 1
        res.save()
    else:
        Record.objects.create(datetime=datetime[:10], num=1)
    if request.session.get('phone_number'):
        phone_number = request.session.get('phone_number')
        user_info = Users.objects.get(phone_number=phone_number)
    else:
        user_info = 0
    return render(request, "home.html", {'userinfo': user_info})
    # request.session.flush()
    # return HttpResponse(1)


def logout(request):
    request.session.flush()
    return HttpResponse(1)
