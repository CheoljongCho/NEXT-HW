from django.db import models

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
  
class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  content = models.TextField()
  
  def __str__(self):
    return self.content
  
class adComment(models.Model):
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='adcomments')
  adcontent = models.TextField()
  
  def __str__(self):
    return self.adcontent
  
