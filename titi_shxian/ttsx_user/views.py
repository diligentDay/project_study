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
    return render(request,'ttsx_user/login.html')
def index(request):
    return render(request,'ttsx_user/index.html')
