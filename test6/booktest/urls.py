from django.conf.urls import url
import views
urlpatterns = [
    url('^$',views.index),
    url('^pic1/$',views.pic1),
    url('^pic2/$',views.pic2),
    url('^pic3/$',views.pic3),
    url('^page(\d*)/$',views.pagelist),
    url('^area1/$',views.area1),
    url('^sheng/$',views.sheng),
    url('^shi/$',views.shi),
    
]

