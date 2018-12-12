# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField(null=True)
    phone=models.CharField(max_length=20,null=True)
    apartment=models.CharField(max_length=30,null= True)
    address=models.CharField(max_length=30,null= True)
    interest=models.CharField(max_length=20,null=True)
@receiver(post_save,sender =User)
def create_UserInfo(sender,instance,created,**kwargs):
    if created:
        UserInfo.objects.get_or_create(user=instance)
class Diary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    diary=models.TextField()
    cost=models.FloatField()
    weight=models.FloatField()
    def __unicode__(self):
        return self.user.username+';'+str(self.date)+';'+str(self.cost)+';'+str(self.weight)