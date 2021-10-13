"""Определения и конфигурации моделей приложения posts."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель группы публикации."""
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Максимальная длинна 200 символов',
    )
    slug = models.SlugField(unique=True, verbose_name='Путь')
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    """Модель публикации."""
    text = models.TextField(verbose_name='Текст публикации')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='По умолчанию: текущая дата/время'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа публикаций'
    )

    class Meta:
        ordering = ('-pub_date',)
