"""Настройки URL приложения yatube"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls, name='admin_page'),
]
