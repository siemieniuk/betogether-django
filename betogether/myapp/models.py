from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now=True)

class Post(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    time_created = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)

class Comment(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=500)