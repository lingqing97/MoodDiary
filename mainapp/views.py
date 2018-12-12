# -*- coding: utf-8 -*-
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
from django.contrib.auth.models import User
from defclass import *



#show the home page befoe user log in
def show_home(request):
    template=get_template('home.html')
    html=template.render(locals())
    return HttpResponse(html)

#to deal the login page
def loginauth(request):
    template=get_template('loginauth.html')
    username=None
    if request.user.is_authenticated():
        user=request.user
        diaries = Diary.objects.filter(user=user)
        template = get_template('user_home.html')
        username=request.user.username
    else:
        if request.method=='GET':
            loginform=LoginForm()
        else:
            loginform=LoginForm(request.POST)
            if loginform.is_valid():
                username=auth.authenticate(request,username=loginform.cleaned_data['username'],password=loginform.cleaned_data['password'],age=0,interest='',birthday='',phone='')
                if username and username.is_active:
                    user=User.objects.filter(username=username)
                    diaries = Diary.objects.filter(user=user)
                    template = get_template('user_home.html')
                    auth.login(request,username)
                else:
                    username=None
                    messages.add_message(request,messages.WARNING,'密码错误或账号未注册')
            else:
                username=None
                messages.add_message(request,messages.WARNING,'请输入完整的账号和密码')
    html=template.render(locals(),request)
    return HttpResponse(html)
#define the function to deal the user logout
def logoutauth(request):
    template=get_template('home.html')
    auth.logout(request)
    messages.add_message(request,messages.INFO,'成功注销了')
    html=template.render(locals(),request)
    return HttpResponse(html)
#define the function to show the main page of user
def show_user_home(request):
    if request.user.is_authenticated():
        template=get_template('user_home.html')
        username=request.user.username
        user=User.objects.filter(username=username)
        diaries = Diary.objects.filter(user=user)
        html=template.render(locals())
    else:
        return HttpResponseRedirect('/')
    return HttpResponse(html)
#define the function to show the user's information
#and allow the user to change his information
def showinfo(request):
    if request.user.is_authenticated():
        username = User.objects.get(username=request.user.username).username
        email = User.objects.get(username=request.user.username).email
        if UserInfo.objects.filter(user=request.user).exists():
            user = UserInfo.objects.get(user=request.user)
        else:
            user=None
        if request.method=='GET':
            newuser_info=userinfo()
            template=get_template('user_showinfo.html')
            html=template.render(locals(),request)
            return HttpResponse(html)
        else:
            newuser_info = userinfo(request.POST)
            if newuser_info.is_valid():
                messages.add_message(request, messages.INFO, '修改成功')
                UserInfo.objects.filter(user=request.user).update(age=newuser_info.cleaned_data['age']\
                    ,phone=newuser_info.cleaned_data['phone'],apartment=newuser_info.cleaned_data['apartment']\
                    ,address=newuser_info.cleaned_data['address'],interest=newuser_info.cleaned_data['interest'])
                return HttpResponseRedirect('/showinfo/')
            else:
                messages.add_message(request, messages.WARNING, '修改失败')
                return HttpResponseRedirect('/showinfo/')
    else:
        return HttpResponseRedirect('/')
#define the function to make the user post diaries
def post(request):
    if request.user.is_authenticated():
        template = get_template('write_diary.html')
        if request.method=='GET':
            newdiary=NewDiary()
            html=template.render(locals(),request)
        else:
            user=request.user
            diary_form=Diary(user=user)
            newdiary = NewDiary(request.POST,instance=diary_form)
            if newdiary.is_valid():
                messages.add_message(request, messages.INFO,'提交成功')
                newdiary.save()
                html=template.render(locals(),request)
            else:
                messages.add_message(request, messages.INFO, '提交失败')
                html=template.render(locals(),request)
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('/')




