#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from hashlib import sha1
from models import *
import datetime
# Create your views here.
def register(request):
    context={'title':'注册','top':'0'}
    return render(request,'ttsx_user/register.html',context)
def register_handle(request):
    #接收数据
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    umail = post.get('user_email')
    #加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1=s1.hexdigest()

    #创建对象
    user=HeroInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.umail = umail
    user.save()
    #完成后转向
    return redirect('/user/login/')
def register_valid(request):
    uname = request.GET.get('uname')
    #获取用户名的总数id
    result=HeroInfo.objects.filter(uname=uname).count()
    context={'valid':result}
    return JsonResponse(context)    
def login(request):
    #不知这句话为什莫这么写，我认为是在让浏览器保存用户名并获取
    uname=request.COOKIES.get('uname','')
    print(type(request.COOKIES))
    print(request.COOKIES)
    print(dir(request.COOKIES))
    contest={'title':'登录','uname':uname,'top':'0'}
    return render(request,'ttsx_user/login.html',contest)
def login_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uname_jz = post.get('uname_jz','0')#不明白神魔意思

    #加密
    s1=sha1()
    s1.update(upwd)
    upwd_sha1=s1.hexdigest()
    
    context = {'title':'登录','uname':uname,'upwd':upwd,'top':'0'}#不明白神魔意思
    users = HeroInfo.objects.filter(uname=uname)
    if len(users) == 0:
        #用户名错误
        context['name_error']='1'#不懂
        return render(request,'ttsx_user/login.html',context)
    else:
        #用户名存在
        print(issubclass(type(users),list))
        print(issubclass(type(users),dict))
        print(type(users))
        print(users)
        print(dir(users))
        if users[0].upwd==upwd_sha1:#登录成功
            #记录当前登录的用户
            request.session['uid']=users[0].id #不懂
            #记主用户名
            response=redirect('/user/')
            if uname_jz=='1':
                response.set_cookie('uname',uname,expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set_cookie('uname','',max_age=-1)
            return response
        else:
           #密码错误 
            context['pwd_error']='1'
            return render(request,'ttsx_user/login.html',context)
def center(request):
    context={'title':'用户中心'}
    return render(request,'ttsx_user/user_center_info.html',context)
def index(request):
    return render(request,'ttsx_user/index.html')

def test_res(request):
    a = HttpResponse('ok')
    print(type(a))
    print(a)
    print(dir(a))
    b = JsonResponse({'ok':'1234'})
    print(type(b))
    print(b)
    print(dir(b))
    c = render(request,'ttsx_user/index.html')
    print(type(c))
    print(c)
    print(dir(c))
    return a
