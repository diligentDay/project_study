from django.conf.urls import url
import views
urlpatterns=[
    url('^session_test/$',views.session_test),
    url('^bianliang/$',views.bianliang),
    url('^biaoqian/$',views.biaoqian),
    url('^guolvqi/$',views.guolvqi),
    url('^guolvqi2/$',views.guolvqi2),
    url('^zhuanyi/$',views.zhuanyi),
    url('^csrf1/$',views.csrf1),
    url('^csrf2/$',views.csrf2),
    url('^verify_code/$',views.verify_code),
    url('^yzm/$',views.yzm),
    url('^yzm2/$',views.yzm2),
    url('^fan1/$',views.fan1),
    url('^fan/$',views.fan2,name='fan2'),

]
if __name__ == '__main__':
    print('ok')
