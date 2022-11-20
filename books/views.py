from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name: str = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name: str = 'books/book_detail.html'
