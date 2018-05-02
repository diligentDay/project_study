#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from datetime import date

# Create your views here.
#查询所有图书并显示
def index(request):
    list=BookInfo.books.all()
    #list=BookInfo.books.filter(id=1)#执行这三行代码出错
    #list=BookInfo.books.filter(btitle_contains='传')
    #list=BookInfo.books.filter(btitle_endswith='部')
  
    return render(request,'booktest/index.html',{'list':list})

#创建新图书
def create(request):
    book=BookInfo.books.create('流星蝴蝶剑',date(1995,12,30))
    book.save()
    #转向到首页
    return redirect('/')
def delete(request,id):
    book=BookInfo.books.get(pk=int(id))
    book.isDelete=True
    book.save()
    #转到首页
    return redirect('/')
def area(request):
    gz=AreaInfo.objects
    context={'city':gz}
    return render(request,'booktest/area.html',context)
