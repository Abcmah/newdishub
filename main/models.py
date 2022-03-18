from tkinter import CASCADE
from tokenize import group
from venv import create
from django.db import models
from user.models import User
# Create your models here.




class Group(models.Model):
    name = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,related_name="participants",blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    topic = models.CharField(max_length=100,blank=True,null=True)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    creater = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    discription = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.topic[0:50]

class Message(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):

        return self.body[0:20]
