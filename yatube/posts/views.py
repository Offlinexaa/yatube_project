"""Определения отображений приложения posts."""
from re import template
from django.http.request import HttpRequest
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

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


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
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
    # Здесь код запроса к модели и создание словаря контекста
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
