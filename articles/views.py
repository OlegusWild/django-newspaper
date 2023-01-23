from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import Article
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.shortcuts import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
