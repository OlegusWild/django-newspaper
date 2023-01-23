from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # to represent pretty in admin panel
    def __str__(self) -> str:
        return self.title
    
    # redirecting after creating a new instance (instructions where to go after it)
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'  # let us obtain ALL comments in templates related to a given article
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
