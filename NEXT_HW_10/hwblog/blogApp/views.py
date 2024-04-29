from django.shortcuts import render, redirect
from .models import Article, Comment, Reply

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
  
  if request.method == "POST":
    if "comment" in request.POST:
      content = request.POST['content']
      
      new_comment = Comment.objects.create(
        articles=articles,
        content=content,
      )
    
    elif "reply" in request.POST:
      comment_id = request.POST['comment_id']
      comment = Comment.objects.get(id=comment_id)
      content = request.POST['content']
      
      new_reply = Reply.objects.create(
        comment=comment,
        content=content,
      )
      
  return render(request, 'list.html', {'articles': articles, 'categories': categories, 'category_counts': category_counts})

def detail(request, article_id):
  article = Article.objects.get(id = article_id)
  comments = Comment.objects.filter(article=article)

  
  if request.method == 'POST':
    if "comment" in request.POST:
      content = request.POST['content']
      
      new_comment = Comment.objects.create(
        article=article,
        content=content,
      )

    elif "reply" in request.POST:
      comment_id = request.POST['comment_id']
      comment = Comment.objects.get(id=comment_id)
      content = request.POST['content']
      
      new_reply = Reply.objects.create(
        comment=comment,
        content=content,
      )
    
    return redirect('detail', article_id=article_id)

  return render(request, 'detail.html', {'article': article, 'comments': comments})
    

def delete(request, article_id):
  article = Article.objects.get(id=article_id)
  article.delete()
  return redirect('detail', article_id)

def delete_comment(request, article_id, comment_id):
  comment = Comment.objects.get(id=comment_id)
  reply_cnt = Reply.objects.filter(comment=comment).count()
  
  if reply_cnt > 0:
    comment.content = '삭제된 댓글입니다.'
    comment.save()
  else:
    comment.delete()
  
  return redirect('detail', article_id=article_id)

def delete_reply(request, article_id, comment_id, reply_id):
  reply = Reply.objects.get(id = reply_id)
  reply.delete()
  
  reply_cnt = Reply.objects.filter(comment_id=comment_id).count()
  comment = Comment.objects.get(id=comment_id)
  
  if reply_cnt == 0 and comment.is_deleted:
    comment.delete()
    
  return redirect('detail', article_id)

def category(request, category_id):
  articles = Article.objects.filter(category=category_id)
  category_name = dict(Article.CATEGORY_CHOICES)[category_id]
  return render(request, 'category.html', {'articles':articles, 'category': category_name})

def base(request):
  return render(request, 'base.html')