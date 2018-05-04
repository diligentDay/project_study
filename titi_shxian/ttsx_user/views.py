#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from hashlib import sha1
from models import *
# Create your views here.
def register(request):
    context={'title':'注册'}
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
    user.upwd = upwd
    user.umail = umail
    user.save()
    #完成后转向
    return redirect('/user/login/')
def register_valid(request):
    uname = request.GET.get('uname')
    resule=HeroInfo.objects.filter(uname=uname).count()
    context={'valid':resule}
    return JsonResponse(context)    
def login(request):
    uname=request.COOKIES.get('uname','')
    contest={'title':'登录','uname':uname,'top':'0'}
    return render(request,'ttsx_user/login.html',contest)
def login_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uname_jz = post.get('uanme_jz','0')#不明白神魔意思

    #加密
    s1=sha1()
    s1.update(upwd)
    upwd_sha1=s1.hexdigest()
    
    context = {'title':'登录','uname':uname,'upwd':upwd,'top':0}#不明白神魔意思
    users = HeroInfo.objects.filter(uname=uname)
    if len(users) == 0:
        context['name_eror'='1']
        return render(request,'ttsx_user/login.html',context)
    else:
        if users[0].upwd==upwd_sha1:#登录成功
            #记录当前登录的用户
            request.session['uid']=users[0].id
            #记主用户名
            response=redirect('/user/')
            if uname_jz=='1':
                response.set_cookie('uname',uname,expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set)cookie('uname',',max_age=-1')
            return response
        else:
           #密码错误 
            context['pwd_error']='1'
            return render(request,'ttsx_user/login.html',context)

def index(request):
    return render(request,'ttsx_user/index.html')
