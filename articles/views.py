from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import Article
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'author')
    template_name = 'article_create.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
