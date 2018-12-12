# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.template import *
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django import forms
from django.contrib import messages
from django.contrib import auth
from .models import Diary
from django.forms import Textarea
from .models import UserInfo
# from .models import NewUser
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username=forms.CharField(label='姓名',max_length=20)
    password=forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput())

class userinfo(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['age','phone','apartment','address','interest']
    def __init__(self,*args,**argv):
        forms.ModelForm.__init__(self,*args,**argv)
        self.fields['age'].label='年龄:'
        self.fields['phone'].label='手机号:'
        self.fields['apartment'].label='部门:'
        self.fields['address'].label='住址:'
        self.fields['interest'].label='兴趣:'

class NewDiary(forms.ModelForm):
    class Meta:
        model=Diary
        fields=['diary','cost','weight']
        widgets={'diary':Textarea(attrs={'cols':80,'rows':10,'vertical-align':'bottom'}),
                 }
    def __init__(self,*args,**argv):
        forms.ModelForm.__init__(self,*args,**argv)
        self.fields['diary'].textarea='日记:'
        self.fields['cost'].label='今日花费:'
        self.fields['weight'].label='今日体重:'