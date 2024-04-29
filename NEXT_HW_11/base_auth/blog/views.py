from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Comment, Post
from django.contrib.auth.decorators import login_required
from authapp.permissions import check_is_creator_or_admin
from .decorators import save_access_info


def home(request):
    posts = Post.objects.all()

    return render(request, "home.html", {"posts": posts})


@login_required
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        new_post = Post.objects.create(
            title=title, content=content, creator=request.user
        )
        return redirect("detail", new_post.pk)

    return render(request, "new.html")

@login_required
def detail(request, post_pk, current_user=None, current_time=None):
    post = Post.objects.get(pk=post_pk)
    last_user = request.session.get('last_user')
    last_access_time = request.session.get('last_access_time')
    
    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(post=post, content=content, creator=request.user)
        
        # 마지막으로 접근한 사용자 정보 업데이트
        post.update_last_access_info(request.user.username)
        
        return redirect("detail", post_pk)

    return render(request, "detail.html", {"post": post, "current_user": current_user, "current_time": current_time, "last_user": last_user, "last_access_time": last_access_time})


@login_required
@check_is_creator_or_admin(Post, "post_pk")
def edit(request, post_pk, current_user=None, current_time=None):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        
        # 사용자가 입력한 값을 가져와서 세션에 저장합니다.
        new_user = request.POST.get("username")
        new_access_time = request.POST.get("access_time")
        
        if new_user:
            current_user = new_user
        if new_access_time:
            current_time = new_access_time
        
        return redirect("detail", post_pk)

    return render(request, "edit.html", {"post": post, "current_user": current_user, "current_time": current_time})

@login_required
@check_is_creator_or_admin(Post, "post_pk")
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("home")


@login_required
@check_is_creator_or_admin(Comment, "comment_pk")
def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect("detail", post_pk)