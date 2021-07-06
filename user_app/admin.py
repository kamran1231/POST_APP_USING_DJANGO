from django.contrib import admin

from .models import User_Post
# from . models import User
# Register your models here.


@admin.register(User_Post)
class POSTAdmin(admin.ModelAdmin):
    list_display = ['id','user','text','created_at','updated_at']
