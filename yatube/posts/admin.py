"""Настройки админки для приложения posts."""
from django.contrib import admin

from yatube.settings import EMPTY_VALUE_PLACEHOLDER
from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    """Настройка отображения модели Post в админке."""
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group', )
    search_fields = ('text', )
    list_filter = ('pub_date', )
    empty_value_display = EMPTY_VALUE_PLACEHOLDER


class GroupAdmin(admin.ModelAdmin):
    """Настройка отображения модели Group в админке."""
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title', 'slug')
    empty_value_display = EMPTY_VALUE_PLACEHOLDER


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
