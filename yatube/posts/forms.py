from typing import Text
from django import forms
from django.forms import fields

from .models import Group, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].requred = True
