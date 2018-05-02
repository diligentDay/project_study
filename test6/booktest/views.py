from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import *
# Create your views here.
def index(request):
    return render(request,'booktest/index.html')
def pic1(request):
    return render(request,'booktest/pic1.html')
def pic2(request):
    f1=request.FILES['f1']
    f1_path='%s/booktest/%s'%(settings.MEDIA_ROOT,f1.name)
    with open(f1_path,'w') as pic:
        for c in f1.chunks():
            pic.write(c)
    p1=PicTest()
    p1.pic='booktest/%s'%f1.name
    p1.save()
    return HttpResponse('ok')
def pic3(request):
    pList=PicTest.objects.all()
    context={'plist':pList}
    return render(request,'booktest/pic3.html',context)

def pagelist(request,pindex):
    sheng=AreaInfo.objects.filter(aParent__isnull=True)
    paginator=Paginator(sheng,10)
    page=paginator.page(int(pindex))
    if pindex=='':
        pindex='1'
    return render(request,'booktest/pagelist.html',{'page':page})
def area1(request):
    return rebder(request,'booktest/area1.html')
def sheng(request):
    shenglist=AreaInfo.objects.filterr(aParent_isnull=True)
    list=[]
    for s in shenglist:
        list.append([s.id,s.atitle])
    return JsonResponse({'list':shenglist})
def shi(request):
    sid=request.GET.get('sid')
    shilis=AreaInfo.objects.filter(aParent_id=sid)
    list=[]
    for s in shilist:
        list.append({'id':s.id,'title':s.atitle})
    return JsonResponse({'list':lislt})

