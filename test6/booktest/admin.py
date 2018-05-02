#coding=utf-8
from django.contrib import admin
from models import *

# Register your models here.
class AreaInline(admin.StackedInline):
    model = AreaInfo
    extra = 2
class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id','atitle','aParent','title']
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['atitle']
    list_filter = ['atitle']
    # fields = ['aParent','atitle']
    fieldsets = [
        ('基本',{'fields':['atitle']}),
        ('高级',{'fields':['aParent']})
]
    inlines = [AreaInline]
admin.site.register(AreaInfo,AreaAdmin)
admin.site.register(PicTest)
