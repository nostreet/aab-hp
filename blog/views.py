from django.shortcuts import render
from blog.models import Post, Image
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PostListView(LoginRequiredMixin,ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(created_date__lt=timezone.now()).order_by('-created_date')

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

    def get_context_data(self, **kwargs):

        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["img_list"] = Image.objects.all()
        return context
