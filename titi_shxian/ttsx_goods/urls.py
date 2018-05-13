from django.conf.urls import  url,include
import views
urlpatterns = [
    url('^$',views.index),
    url(r'list(\d+)_(\d+)_(\d+)/$',views.goods_list),
    url('^(\d+)/$',views.detail),
    url(r'^search/',include('haystack.urls')),
    #url('^cart/$',views.cart),
] 
