from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    objects = models.Manager()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='poster')
    title = models.CharField(max_length=52)
    text = models.TextField()


    def __str__(self):
        return self.title
    