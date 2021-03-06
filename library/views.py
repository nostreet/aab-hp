from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookListView(LoginRequiredMixin,ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.order_by('title')
