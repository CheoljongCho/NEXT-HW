from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser,
  BaseUserManager,
  PermissionsMixin,
)

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  CATEGORY_CHOICES = [
    ('Hobby', '취미'),
    ('Food', '음식'),
    ('Programming', '프로그래밍'),
  ]
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
  reg_time = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
  
  def comment_count(self):
    return self.comments.filter(is_deleted=False).count()
  
class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  content = models.TextField()
  is_deleted = models.BooleanField(default=False)
  
  def __str__(self):
    return self.content
  
class Reply(models.Model):
  content = models.TextField()
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
  
  def __str__(self):
    return self.content

