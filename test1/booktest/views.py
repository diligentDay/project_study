#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from models import BookInfo
# Create your views here.
def index(request):
    #查询所有图书
    booklist = BookInfo.objects.all()
    print(booklist)
    #将图书列表传递到模块中，然后渲染模板
    return render(request,'booktest/index.html',{'booklist':booklist, 'www':789})
#详情页，接收图书的编号，根据编号查询，再过关系找到本图书的所有英雄展示
def detail(request,id):
    #根据图书编号对应图书
    book = BookInfo.objects.get(pk=id)
    #将图书信息传递到模块中然后渲染
    return render(request,'booktest/detail.html',{'book':book})


