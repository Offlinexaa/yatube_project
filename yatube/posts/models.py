"""Определения и конфигурации моделей приложения posts."""
from django.db import models
from django.contrib.auth import get_user_model


# Модель User используем 'как есть'
User = get_user_model()


# Модель Group вынесена в начало, чтобы не раздражать линтер
class Group(models.Model):
    """Модель группы публикации.\n
    Поля:\n
    title - название группы;\n
    slug - строка для подстановки в url;\n
    description - развёрнутое описание группы."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)


class Post(models.Model):
    """Модель публикации.\n
    Поля:\n
    text - текст публикации;\n
    pub_date - дата публикации (по умолчанию: текущее дата/время)\n
    autor - pk из модели User;\n
    group - pk из модели Group."""
    text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True
    )
