#coding:utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    #url(r'^(\d+)_(\d+)',views.detail),
    url(r'^(?P<id>\d+)_(?P<pk>\d+)/$',views.detail),
    url('^method1/$',views.method1),
    url('^method2/$',views.method2),
    url('^method3/$',views.method3),
    url('^get1/$',views.get1),
    url('^get2/$',views.get2),
    url('^get3/$',views.get3),
    url('^post1/$',views.post1),
    url('^post2/$',views.post2),
 
    url('^json1/$',views.json1),
    url('^json2/$',views.json2),
    url('^cookie_test/$',views.cookie_test),
]
