import datetime
from django.db import models
from django import forms
from django.forms import widgets

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    duedate = models.DateField(default=datetime.date.today)
    Dday = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
