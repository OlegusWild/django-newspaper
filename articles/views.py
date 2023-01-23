import re

from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import Article, Comment
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.shortcuts import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


COMMENT_CREATE_URL_PATTERN = re.compile(r'(\d+)\/add_comment')

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self) -> bool:
        cur_article_obj = self.get_object()
        return self.request.user == cur_article_obj.author

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_create.html'

    # Do not offer to choose any user
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user  # setting actual logged-in user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'

    def test_func(self) -> bool:
        cur_article_obj = self.get_object()
        return self.request.user == cur_article_obj.author

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('comment',)
    template_name = 'comment_create.html'

    # def get_context_data(self, **kwargs):
    #     print(kwargs)
    #     self.article_id = int(kwargs['id'])

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user  # setting user

        request_path = self.request.path
        article_id = int(COMMENT_CREATE_URL_PATTERN.findall(request_path)[0])
       
        form.instance.article = Article.objects.get(id=article_id)  # setting linked article
        return super().form_valid(form)