"""Определения отображений приложения posts."""
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request: HttpRequest) -> HttpResponse:
    """Отображение главной страницы."""
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts,
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Отображение группы публикаций.\n
    При попытке выбрать несуществующую группу вернёт ошибку 404."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
