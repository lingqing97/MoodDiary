"""MoodDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainapp.views import show_home
from mainapp.views import loginauth
from mainapp.views import logoutauth
from mainapp.views import showinfo
from mainapp.views import show_user_home
from mainapp.views import post
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$',show_home),
    url(r'home/login/',loginauth),
    url(r'^user/home/',show_user_home),
    url(r'^logoutauth/',logoutauth),
    url(r'^showinfo/',showinfo),
    url(r'post/',post),
]