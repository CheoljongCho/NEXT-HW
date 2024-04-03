from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  CATEGORY_CHOICES = [
    ('Habit', '취미'),
    ('Food', '음식'),
    ('Programming', '프로그래밍'),
    ('none', '기타'),
  ]
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
  
  def __str__(self):
    return self.title