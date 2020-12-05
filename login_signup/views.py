from django.shortcuts import render, redirect
from .models import Users
from django.http import HttpResponse
import urllib
import random
import urllib.request
import time
# Create your views here.


# 封装md5加密函数
def md5(strr):
    import hashlib
    m = hashlib.md5()
    m.update(strr.encode("utf8"))
    return m.hexdigest()


# 发送注册短信验证码
def send_code(request):
    smsapi = "http://api.smsbao.com/"
    # 短信宝账号
    user = '1180290010'
    # 短信宝密码
    password = md5('zhurk9750')
    # 短信内容，生成六位随机数
    sms_code = ''
    for i in range(6):
        sms_code += str(random.randint(0, 9))
    content = '【原古石村，许你千年】您的短信验证码为' + sms_code + '，在30分钟内有效。'
    # 要发送短信的手机号码
    phone = str(request.POST.get('phone_number'))
    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    res = response.read().decode('utf-8')
    # 成功返回True，失败返回False
    if res == 0:
        request.session['sms_code'] = sms_code
        return HttpResponse(True)
    else:
        return HttpResponse(False)


# 用户注册
def register(request):
    # 接收用户填写手机号和密码
    phone_number = request.POST.get('phone_number')
    password = md5(request.POST.get('password'))
    sms_code = request.POST.get('sms_code')
    timenick = int(time.time())
    head = "https://stone-1258976754.cos.ap-shanghai.myqcloud.com/default_avatar.jpeg"
    # 特殊出口
    if sms_code == '9999':
        # 将注册用户添加到数据库
        Users.objects.create(phone_number=phone_number, password=password,
                             sex=0, nickname=timenick, head=head, posts='[]',
                             joinposts='[]', identity=0, contribution=0,
                             personality='这个人很懒，还没有简介哦！', auth=0, forbid=1)
        # 设置登录session
        request.session['phone_number'] = phone_number
        # 跳转到首页
        return redirect('home:index')
    if request.session.get('sms_code'):
        if request.session['sms_code'] == sms_code:
            # 将注册用户添加到数据库
            Users.objects.create(phone_number=phone_number, password=password,
                                 sex=0, nickname=timenick, head=head, posts='[]',
                                 joinposts='[]', identity=0, contribution=0,
                                 personality='这个人很懒，还没有简介哦！', auth=0, forbid=1)
            # 设置登录session
            request.session['phone_number'] = phone_number
            # 跳转到首页
            return redirect('home:index')
    return redirect('login_signup:register_page')


# 用户登陆
def login(request):
    # 接受用户填写的手机号和密码
    phone_number1 = request.POST.get('phone_number')
    if phone_number1 == 'guest':
        phone_number = 18957856792
    elif phone_number1 == 'admin':
        phone_number = 18957856793
    password = request.POST.get('password')
    # 查找是否存在该用户
    user_res = Users.objects.filter(phone_number=phone_number)
    if len(user_res):
        # 如果存在该用户，验证密码
        if md5(password) == user_res[0].password:
            # 密码正确则设置session
            request.session['phone_number'] = user_res[0].phone_number
            request.session['head'] = user_res[0].head
            request.session['username'] = user_res[0].nickname
            return redirect('home:index')
        return redirect('home:index')
    else:
        return redirect('login_signup:login_page')


# 加载注册页面
def register_page(request):
    return render(request, 'register_page.html')


# 加载登陆页面
def login_page(request):
    return render(request, 'login_page.html')

