#coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)#标题名称
    isDelete=models.BooleanField(default=False)#删除默认不删
    def __str__(self):
        return self.ttitle.encode('utf-8')#解码
class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=50)#用商品名称
    gpic=models.ImageField(upload_to='goods')#对上传的内容进行校验，确定有图
    gprice=models.DecimalField(max_digits=5,decimal_places=2)#十进制浮点数价格
    gclick=models.IntegerField(default=0)#整数 点击量
    gunit=models.CharField(max_length=20)#单位
    isDelete=models.BooleanField(default=False)#布尔类型
    gsubtitle=models.CharField(max_length=200)#副标题
    gkucun=models.IntegerField(default=100)#整数 库存
    gcontent=HTMLField()#不知道
    gtype=models.ForeignKey('TypeInfo')#一对多
