from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1  # how many empty rows-templates to display

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
