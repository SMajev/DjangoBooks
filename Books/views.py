from django.views.generic import ListView
from .models import Book

class BooksView(ListView):
    template_name = 'books.html'
    model = Book
    context_object_name = 'books'


