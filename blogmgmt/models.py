# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone


class Post(models.Model):
    key = models.CharField(max_length=32,default=uuid.uuid4, editable=False)
    message = models.TextField(max_length=4000)
    title = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default="", null=True,blank=True)

class Comment(models.Model):
    key = models.CharField(max_length=32,default=uuid.uuid4, editable=False)
    comment_text = models.TextField(max_length=4000)
    commented_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, default="", null=True,blank=True)

class Image(models.Model):
    key = models.CharField(max_length=32,default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, default="", null=True,blank=True)

class Like(models.Model):
    key = models.CharField(max_length=32,default=uuid.uuid4, editable=False)
    liked_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(User, default="", null=True,blank=True)
