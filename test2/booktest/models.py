#coding:utf-8
from django.db import models

# Create your models here.
#图书管理器
class BookInfoManager(models.Manager):
    def get_queryset(self):
        #默认查询未删除的图书信息
        #调用父亲的成员语法为：super(子类行,self).成员
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    #创建模型类，接受参数为属性赋值
    def create(self,title,pub_date):
        #创建模型类对象self.model可以获得模型类
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcommet = 0
        book.isDelete = False
        return book
    
# 定义图书模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#图书名称
    bpub_date = models.DateField()#发布日期
    bread = models.IntegerField(default=0)#阅读量
    bcommet = models.IntegerField(default=0)#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除
    books = BookInfoManager()                            
    class Meta:#元信息类
        db_table='bookinfo'
    def __str__(self):
        return self.btitle
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄姓名
    haender = models.BooleanField(default=True)#英雄性别
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcontent = models.CharField(max_length=100)#英雄描述信息
    hbook = models.ForeignKey('BookInfo')#英雄与图书表的关系为一对多，所以属性定义在英雄型中

class AreaInfo(models.Model):
    atitle=models.CharField(max_length=30)
    aParent=models.ForeignKey('self',null=True,blank=True)

