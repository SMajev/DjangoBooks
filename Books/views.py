from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm, BookImportForm
from .google_api import GoogleAPI

class BooksView(ListView):
    template_name = 'books.html'
    model = Book
    context_object_name = 'books'

class BookCreate(CreateView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        Book.objects.create(
            title = cd['title'],
            author = cd['author'],
            published_date = cd['published_date'],
            isbn = cd['isbn'],
            print_length = cd['print_length'],
            cover = cd['cover'],
            language = cd['language']
        )
        return result

class BookImport(FormView):
    template_name = 'google_api_form.html'
    form_class = BookImportForm
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        result = super().form_valid(form)
        google_api = GoogleAPI()
        cd = form.cleaned_data
        phrase = cd['title']
        book = google_api.get_book(phrase)
        Book.objects.create(
            title = book['title'],
            author = book['author'],
            published_date = book['published'],
            isbn = book['isbn'],
            print_length = book['print_length'],
            cover = book['cover'],
            language = book['language']
        )
        return result
