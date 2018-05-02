#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
# Create your views here.
#def detail(request,id1,id2):
    #context={'id1':id1,'id2':id2}
    #return render(request,'booktest/detail.html',context)
def index(request):
    str='%s--%s'%(request.path,request.encoding)
    return HttpResponse(str)
def detail(request,id,pk):
    context={'id1':pk,'id2':id}
    return render(request,'booktest/detail.html',context)
def method1(request):
    return render(request,'booktest/method1.html')
def method2(request):
    return HttpResponse(request.method)
def method3(request):
    return HttpResponse(request.method)
def get1(request):
    return render(request,'booktest/get1.html')
def get2(request):
    dict=request.GET
    a=dict.get('a')
    b=dict.get('b')
    c=dict['c']
    str='%s--%s--%s'%(a,b,c)
    return HttpResponse(str)
def get3(request):
    dict=request.GET
    #a=dict.get('a')
    a=dict.getlist('a')
    b=dict['b']
    c=dict.get('c','no')
    str='%s--%s--%s'%(a,b,c)
    return HttpResponse(str)
def post1(request):
    return render(request,'booktest/post1.html')
def post2(request):
    dict=request.POST
    uname=dict.get('uname')
    upwd=dict.get('upwd')
    ugender=dict.get('ugender')
    uhobby=dict.getlist('uhobby','no')
    str='%s--%s--%s--%s'%(uname,upwd,ugender,uhobby)                    
    return HttpResponse(str)

def json1(request):
    return render(request,'booktest/json1.html')
def json2(request):
    list=BookInfo.objects.all()
    list1=[]
    for book in list:
        list1.append({'btitle':book.btitle})
    return JsonResponse({'list':list1})
def cookie_test(request):
    response=HttpResponse()
    response.write('<h1>hello</h1>')
    #response.set_cookie('h1','hello')
    print(request.COOKIES['h1'])
    return response
