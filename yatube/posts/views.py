"""Определения отображений приложения posts."""
from django.http.request import HttpRequest
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


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
