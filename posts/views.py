from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    select1_user_count = post.select1_user.count()
    select2_user_count = post.select2_user.count()
    context = {
        'post': post,
        'select1_user_count':select1_user_count,
        'select2_user_count':select2_user_count,
    }
    return render(request, 'posts/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 저장 x, 인스턴스만 생성
            post = form.save(commit=False)
            post.user = request.user
            # 저장
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)

@login_required
def select(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)
    user = request.user
    if user in post.select1_user.all() or user in post.select2_user.all():
        return redirect('posts:detail', post_pk=post_pk)

    if answer == post.select1_content:
        post.select1_user.add(user)
    elif answer == post.select2_content:
        post.select2_user.add(user)
    else:
        return redirect('posts:detail', post_pk=post_pk)

    return redirect('posts:detail', post_pk=post_pk)