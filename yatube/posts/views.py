import os
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Последние обновления на сайте',
        'text': 'Информация на главной странице будет тут.',
    }
    template = os.path.join('posts', 'index.html')
    return render(request, template, context)


def group_posts(request, slug):
    context = {
        'title': 'Записи сообщества',
        'text': 'Информация на странице группы будет тут.',
    }
    template = os.path.join('posts', 'group_list.html')
    return render(request, template, context)
