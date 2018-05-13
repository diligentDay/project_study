#coding=utf-8
from django.db import models

# Create your models here.
class HeroInfo(models.Model):
    uname = models.CharField(max_length=20)#姓名
    upwd = models.CharField(max_length=40)#密码
    umail = models.CharField(max_length=20)#邮箱
    ushou = models.CharField(default='',max_length=10)#收件人
    udd = models.CharField(default='',max_length=100)#地址
    ubia = models.CharField(default='',max_length=6)#邮编
    uphone = models.CharField(default='',max_length=11)#手机号
    
