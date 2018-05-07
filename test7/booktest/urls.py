from django.conf.urls import url
import views
urlpatterns=[
    url('^editor/$',views.editor),
    url('^editor2/$',views.editor2),
    url('^editor3/$',views.editor3),
    url('^query/$',views.query),
]
