from django.contrib import admin

# Register your models here.
from app.models import *



class customizewebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['name','url']
    list_editable=['email']
    list_filter=('url',)
    search_fields=['name']
    list_per_page=1

admin.site.register(Topic)
admin.site.register(Webpage,customizewebpage)
admin.site.register(AccessRecord)


