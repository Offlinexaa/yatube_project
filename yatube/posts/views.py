"""Определения отображений приложения posts."""
from datetime import date

from django.http.request import HttpRequest
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User


def index(request: HttpRequest) -> HttpResponse:
    """Отображение главной страницы."""
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'page_obj': page_obj,
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Отображение группы публикаций.\n
    При попытке выбрать несуществующую группу вернёт ошибку 404."""
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)

# @login_required
def profile(request, username):
    author = User.objects.get(username=username)
    post_list = author.posts.all()
    total_posts = len(post_list)
    paginator = Paginator(post_list, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'author': author,
        'total_posts': total_posts,
        'page_obj': page_obj,
    }
    template = 'posts/profile.html'
    return render(request, template, context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    author = post.author
    post_count = author.posts.count()
    if len(post.text) > 30:
        post_head_part = post.text[:30]
    else:
        post_head_part = post.text
    
    context = {
        'post': post,
        'post_count': post_count,
        'post_head_part': post_head_part,
    }
    return render(request, 'posts/post_detail.html', context) 


# @login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = request.user
            pub_date = date.today()
            text = form.cleaned_data['text']
            group = form.cleaned_data['group']
            # Добавлено для формы, не опирающейся на модель
            group = Group.objects.get(pk=group)
            # ---------------------------------------------
            if group == '':
                group = None
            Post.objects.create(
                author=author,
                pub_date=pub_date,
                group=group,
                text=text,
            )
            return redirect(f'/profile/{author.username}/')
        context = {
            'form': form,
        }
        return render(request, 'posts/create_post.html', context)
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)


# @login_required
def post_eidt(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    if post.author != user:
        return redirect(f'/posts/{post_id}')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/posts/{post_id}')
        context = {
            'form': form,
            'is_edit': True,
        }
        return render(request, 'posts/create_post.html', context)
    form = PostForm(initial={'text': post.text, 'group': post.group.pk})
    context = {
        'form': form,
        'is_edit': True,
    }
    return render(request, 'posts/create_post.html', context)