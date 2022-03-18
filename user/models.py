from email.policy import default
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dp = models.ImageField(upload_to='static/profile',null=True, blank=True,default='static/profile/person.svg')
    level = models.CharField(max_length=100,null=True,blank=True)
    institution = models.CharField(max_length=100,null=True,blank=True)
    town = models.CharField(max_length=100,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)

class Text_post(models.Model):
    creater = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:60]

class Comment(models.Model):
    creater = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    text_post = models.ForeignKey(Text_post,on_delete=models.CASCADE,blank=True,null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[0:50]

class Photo_post(models.Model):
    creater = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    photo = models.ImageField(upload_to='static/posts')
    text = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.photo)

class Comment_photo_post(models.Model):
    creater = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    photo_post = models.ForeignKey(Photo_post,on_delete=models.CASCADE,null=True,blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text[0:20]

class Likes(models.Model):
    liker = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Photo_post,on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)