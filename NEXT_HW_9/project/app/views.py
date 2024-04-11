from django.shortcuts import render, redirect
from .models import Post
from datetime import date, datetime
# Create your views here.

def list (request, status=None):
  posts = Post.objects.all()
  today = date.today()
  for post in posts:
    post.Dday = (post.duedate - today).days
  
  sorted_posts = sorted(posts, key=lambda x: x.Dday)
  
  return render(request, 'list.html', {'posts': sorted_posts})
  
def new(request):
  if request.method == 'POST':
    
    print(request.POST)
    
    new_post = Post.objects.create(
      title = request.POST['title'],
      content = request.POST['content'],
      duedate = request.POST['duedate'],
    )
    return redirect('list')
  
  return render(request, 'new.html', {'title': Post.title, 'content': Post.title, 'duedate': Post.duedate})

def detail(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  today = date.today()
  post.Dday = (post.duedate - today).days
  
  return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  
  if request.method == 'POST':
    Post.objects.filter(pk=post_pk).update(
      title = request.POST['title'],
      content = request.POST['content'],
      duedate = request.POST['duedate'],
    )
    return redirect('detail', post_pk)
  
  return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  post.delete()
  
  return redirect('list')
  
  
def base(request):
  return render(request, 'base.html')