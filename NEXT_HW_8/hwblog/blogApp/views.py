from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
  if request.method == 'POST':
    
    print(request.POST)
    
    new_article = Article.objects.create(
      title = request.POST['title'],
      content = request.POST['content'],
      category = request.POST['category'],
    )
    return redirect('list')
  
  return render(request, 'new.html', {'categories': Article.CATEGORY_CHOICES})

def list(request):
  categories = Article.CATEGORY_CHOICES
  category_counts = {}
  for category in categories:
      category_counts[category[0]] = Article.objects.filter(category=category[0]).count() 
  articles = Article.objects.all()
  return render(request, 'list.html', {'articles': articles, 'categories': categories, 'category_counts': category_counts})

def detail(request, article_id):
  article = Article.objects.get(id = article_id)
  return render(request, 'detail.html', {'article':article})

def category(request, category_id):
  articles = Article.objects.filter(category=category_id)
  category_name = dict(Article.CATEGORY_CHOICES)[category_id]
  return render(request, 'category.html', {'articles':articles, 'category': category_name})