#coding=utf-8
#这句不懂
from django.shortcuts import redirect
def user_login(func):
    def func1(request,*args,**kvargs):
        if request.session.has_key('uid'):
            return func(request,*args,**kvargs)
        else:
            return redirect('/user/login')
    return func1

