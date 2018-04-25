#coding:utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    #url(r'^$',views.index),
    #url(r'^(\d+)_(\d+)',views.detail),
    url(r'^(?p<id1>\d+)_(?p<pk>\d+)/$',views.detail),
    url('^method1/$',views.method1),
    url('^method2/$',views.method2),
    url('^method3/$',views.method3),
]
