from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# class Group(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.TextField(blank=False, null=False, default='newgroup')
#     description = models.TextField(blank=True, null=True)


class Post(models.Model):
    text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # group = models.ForeignKey(
    #     Group,
    #     on_delete=models.CASCADE,
    #     related_name='posts',
    #     blank=True,
    #     null=True
    # )
