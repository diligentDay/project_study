from django.conf.urls import url
import views
urlpatterns=[
    url('^register/$',views.register),
    url('^register_handle/$',views.register_handle),
    url('^register_valid/$',views.register_valid),
    url('^login/$',views.login),
    url('^login_handle/$',views.login_handle),
    url('^$',views.center),
    url('^index/$',views.index),
    url('^test_res/$', views.test_res)
    
]
