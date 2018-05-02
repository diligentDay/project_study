from django.contrib import admin
from models import *
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(GoodsInfo,GoodsInfoAdmin)
