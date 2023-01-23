from django.urls import path
from django.conf.urls import url
from .views import ArticleListView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView, ArticleCreateView, CommentCreateView
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/add_comment/', CommentCreateView.as_view() , name='comment_add')
    # url(r'^(?P<article_id>\d+)/add_comment/$', CommentCreateView.as_view() , name='comment_add')
]