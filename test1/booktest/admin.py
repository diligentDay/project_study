from django.contrib import admin
from models import BookInfo,HeroInfo
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','btitle','bpub_date']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','hname','hgender','hcontent']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
