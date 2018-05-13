#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    goods_list=[]
    type_list=TypeInfo.objects.all()
    for t1 in type_list:
        nlist=t1.goodsinfo_set.order_by('-id') [0:4]
        clist=t1.goodsinfo_set.order_by('-gclick') [0:4]
        goods_list.append({'t1':t1,'nlist':nlist,'clist':clist}) 
    context = {'title':'首页','glist':goods_list,'cart_show':'1'}
    return render(request,'ttsx_goods/index.html',context)

def goods_list(request,tid,pindex,orderby):#tid,pindex
    try:
        #获取id
        t1=TypeInfo.objects.get(pk=int(tid))
        #升序降序
        new_list=t1.goodsinfo_set.order_by('-id')[0:2]
        #指定排序规则
        orderby_str='-id'
        desc='1'
        if orderby=='2':
            desc=request.GET.get('desc','1')
            if desc=='1':
                orderby_str='-gprice'
            else:
                orderby_str='gprice'
        elif orderby=='3':
            orderby_str='-gclick'
        #查询：当前分类的所有商品，按没页15个来显示
        glist=t1.goodsinfo_set.order_by(orderby_str)
        #分页
        paginator=Paginator(glist,10)
        pindex1=int(pindex)
        if pindex1<1:
            pindex1=1
        elif pindex1>paginator.num_pages:
            pindex1=paginator.num_pages
        page=paginator.page(pindex1)
        context = {'title':'商品列表页','cart_show':'1','t1':t1,\
            'orderby':orderby,'new_list':new_list,'page':page,\
            'desc':desc}
        print(desc)
        print(type(desc))
        print(page)        
        return render(request,'ttsx_goods/list.html',context)
    except Exception as e:
        print(e)
        print(type(e))
        return render(request,'404.html')

def detail(request,id):
    try:
        goods=GoodsInfo.objects.get(pk=int(id))
        goods.gclick+=1
        goods.save()
        new_list=goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        context={'title':'商品详情页','cart_show':'1','goods':goods,'new_list':new_list}
        response=render(request,'ttsx_goods/detail.html',context)
	gids=request.COOKIES.get('goods_ids','').split(',')
        if id in gids:
            gids.remove(id)
        gids.insert(0,id)
        if len(gids)>5: 
            gids.pop()
	response.set_cookie('goods_ids',','.join(gids),max_age=60*60*24*7)
        return response
    except Exception as e:
        return render(request,'404.html')
'''
def cart(request,id):
    goods=GoodsInfo.objects.get(pk=int(id))
    context={'title':'我的购物车','goods':goods}
    return render(request,'ttsx_goods/cart.html',context)
'''

