#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
from PIL import Image, ImageDraw, ImageFont
# Create your views here.
def session_test(request):
    request.session['h1']='hello'
    #h1=request.session['h1']
    #print(h1)
    #del request.session['h1']
    #request.session.flush()
    return HttpResponse('0k')
def bianliang(request):
    dict={'title':'字典'}
    b=BookInfo()
    b.btitle='对象'
    context={'dict':dict,'book':b}
    return render(request,'booktest/bianliang.html',context)

def biaoqian(request):
    list=BookInfo.objects.all()
    context={'book_list':list}
    return render(request,'booktest/biaoqian.html',context)
def guolvqi(request):
    list=BookInfo.objects.all()
    context={'book_list':list}
    return render(request,'booktest/guolvqi.html',context)
def guolvqi2(request): 
    list=BookInfo.objects.all()
    context={'book_list':list}
    return render(request,'booktest/guolvqi2.html',context)

def zhuanyi(request):
    context={'title':'<h1>hello<h1>'}
    return render(request,'booktest/zhuanyi.html',context)
def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    return HttpResponse('ok')

def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # font = ImageFont.truetype('FreeMono.ttf', 23)
    font = ImageFont.truetype('KhmerOSsys.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
def yzm(request):
    return render(request,'booktest/yzm.html')
def yzm2(request):
    yzm1=request.POST.get('yzm')
    if yzm1==request.session['verifycode']:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')
def fan1(request):
    return render(request,'booktest/fan1.html')
def fan2(request):
    return HttpResponse('ok')
