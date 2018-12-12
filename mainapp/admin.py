# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Diary
# from .models import NewUser
import django.contrib
from .models import User
from .models import UserInfo
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('user','cost','weight','date')
    ordering = ['-date',]
    search_fields = ('cost','weight','diary')
    def save_form(self, request, form, change):
        form.user=request.user
        form.save()
    def get_form(self, request, obj=None, **kwargs):
        self.exclude=("user",)
        form=super(DiaryAdmin,self).get_form(request,obj,**kwargs)
        return form
admin.site.register(Diary,DiaryAdmin)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','age','phone')
    ordering = ['age',]
    search_fields = ('age','phone')
admin.site.register(UserInfo,UserInfoAdmin)
