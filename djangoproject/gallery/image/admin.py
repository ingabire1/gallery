from django.contrib import admin
from .models import Editor,Image,location,Category

  # Register your models here.

class imageAdmin(admin.ModelAdmin):
  # filter =('id','location','category')  
    admin.site.register(Editor)
    admin.site.register(Image)
    admin.site.register(location)
    admin.site.register(Category)