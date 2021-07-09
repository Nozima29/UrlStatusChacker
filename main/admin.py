from django.contrib import admin
from .models import UrlModel
# Register your models here.

class URLAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'url']

admin.site.register(UrlModel, URLAdmin)