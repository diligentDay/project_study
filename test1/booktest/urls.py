#coding:utf-8
from django.conf.urls import url
#引入试图模块
from . import views
urlpatterns = [
    #配置首页url
    url(r'^$',views.index),
    #配置详情页url,\d+表示多个数字,小括号用于取值，建议复习下正则表达式
    url(r'^(\d+)/$',views.detail)
]
