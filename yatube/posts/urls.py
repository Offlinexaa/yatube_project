"""Конфигурация URL для приложения posts."""
from django.urls import path
from . import views


# Применяется для указания неймспейса в yatube/urls.py
# pylint утверждает, что константы надо писать в UPPER_CASE ^_^
app_name = 'posts'


# TODO: Придумать, как показать посты без группы
urlpatterns = [
    path('', views.index, name='main_page'),
    path('group/<slug:slug>/', views.group_posts, name='group_page')
]
