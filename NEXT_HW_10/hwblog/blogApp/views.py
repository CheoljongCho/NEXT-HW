from django.shortcuts import render, redirect
from .models import Article, Comment, adComment

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
  comments = Comment.objects.filter(article=article)
  ad_comments = adComment.objects.filter(comment__article=article)
  
  if request.method == 'POST':
    content = request.POST.get('content')  
    if content:  
        new_comment = Comment.objects.create(article=article, content=content)

    adcontent = request.POST.get('adcontent')  
    if adcontent:  
        comment_id = request.POST.get('comment_id')
        parent_comment = Comment.objects.get(id=comment_id)
        new_adcomment = adComment.objects.create(comment=parent_comment, adcontent=adcontent)

    return redirect('detail', article_id=article_id)

  return render(request, 'detail.html', {'article': article, 'comments': comments, 'ad_comments': ad_comments})
    

def delete(request, article_id):
  article = Article.objects.get(id=article_id)
  article.delete()
  return redirect('detail', article_id)

def delete_comment(request, article_id, comment_id):
  comment = Comment.objects.get(id=comment_id)
  comment.delete()
  return redirect('detail', article_id)

def delete_adcomment(request, article_id, comment_id, adcomment_id):
  adcomment = adComment.objects.get(adComment, id=adcomment_id)
  adcomment.delete()
  return redirect('detail', article_id, comment_id)

def category(request, category_id):
  articles = Article.objects.filter(category=category_id)
  category_name = dict(Article.CATEGORY_CHOICES)[category_id]
  return render(request, 'category.html', {'articles':articles, 'category': category_name})