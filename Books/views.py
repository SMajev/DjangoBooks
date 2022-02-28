from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

class BooksView(ListView):
    template_name = 'books.html'
    model = Book
    context_object_name = 'books'

class BookCreate(CreateView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('/')
