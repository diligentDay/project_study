#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
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
    return HttpResponse(request,method)
def method3(request):
    return HttpResponse(request,method)
