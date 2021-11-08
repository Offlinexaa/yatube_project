from django import forms
# from django.forms import fields

from .models import Group


class PostForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(),
        required=True,
        label='Текст поста',
        help_text='Текст нового поста',
    )

    group_dict = {'':'--------',}
    for group in Group.objects.all():
        group_dict.update({group.pk:group.title})
    group = forms.ChoiceField(
        choices=group_dict,
        label='Группа',
        help_text='Группа, к которой будет относиться пост',
    )

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('group', 'text')

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['text'].requred = True
