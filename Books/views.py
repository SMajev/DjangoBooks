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
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Book.objects.create(
            title = cleaned_data['title'],
            author = cleaned_data['author'],
            published_date = cleaned_data['published_date'],
            isbn = cleaned_data['isbn'],
            print_length = cleaned_data['print_length'],
            cover = cleaned_data['cover'],
            language = cleaned_data['language']
        )
        return result
