"""Определения отображений приложения posts."""
import os
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request: HttpRequest) -> HttpResponse:
    """Отображение главной страницы."""
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    template = os.path.join('posts', 'index.html')
    return render(request, template, context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Отображение группы публикаций.\n
    При попытке выбрать несуществующую группу вернёт ошибку 404."""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    template = os.path.join('posts', 'group_list.html')
    return render(request, template, context)
