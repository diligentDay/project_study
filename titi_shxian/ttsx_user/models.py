from django.db import models

# Create your models here.
class HeroInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    umail = models.CharField(max_length=20)
    ushou = models.CharField(default='',max_length=20)
    udd = models.CharField(default='',max_length=100)
    ubia = models.CharField(default='',max_length=6)
    uphone = models.CharField(default='',max_length=11)
    
