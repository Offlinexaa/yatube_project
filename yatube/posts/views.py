import os
from django.shortcuts import render, get_object_or_404

from .models import Group, Post

# Create your views here.


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    template = os.path.join('posts', 'index.html')
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': f'Последние обновления в сообществе {group}',
        'group': group,
        'posts': posts,
    }
    template = os.path.join('posts', 'group_list.html')
    return render(request, template, context)
