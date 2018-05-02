from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def editor(request):
    return render(request,'booktest/editor.html')
def editor2(request):
    e1=request.POST.get('editor1')
    g=GoodsInfo()
    g.gcontent=e1
    g.save()
    return HttpResponse('ok')
def editor3(request):
    glist=GoodsInfo.objects.all()
    context={'list':glist}
    return render(request,'booktest/editor3.html',context)
