from django.contrib import admin
from .models import *

# Register your models here.
class CategroyAdmin(admin.ModelAdmin):
    list_display=('name','image','description')


admin.site.register(Category,CategroyAdmin)
admin.site.register(Products)
