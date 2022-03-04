from django.views.generic import (
    ListView, CreateView, FormView, UpdateView, DetailView, DeleteView,
    TemplateView
)
from django.urls import reverse_lazy, reverse
from django.http import request, Http404
# from django.views.decorators import api_view

from .models import Book
from .forms import BookForm, BookImportForm
from .filters import BookFilter
from .google_api import GoogleAPI
from .serializers import BookSerializer

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView ,ListCreateAPIView


from datetime import datetime as dt

# This is main view which show list all of our books

class BooksView(ListView):
    template_name = 'books.html'
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context  
    
    def get_ordering(self):
        ordering = 'title'
        return ordering
    
    
    

class BookDetailView(DetailView):
    template_name = 'book.html'
    model = Book
    context_object_name = 'book'


class BookCreate(CreateView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        result = super().form_valid(form)
        return result

    

class BookImport(FormView):
    template_name = 'google_api_form.html'
    form_class = BookImportForm
    success_url = reverse_lazy('books')

    def convert_date(self, various_date):
        format_list = [
            "%Y/%m/%d", "%Y-%m-%d", "%Y%m%d",
            "%d/%m/%Y", "%d-%m-%Y", "%d%m%Y",
            "%Y/%m", "%Y-%m", "%Y%m", "%Y", 
        ]
        for fmt in format_list:
            try:
                return dt.strptime(various_date, fmt).date()
            except ValueError:
                continue
        raise ValueError(various_date)


    def form_valid(self, form):
        result = super().form_valid(form)
        google_api = GoogleAPI()
        cd = form.cleaned_data
        phrase = cd['phrase']
        book = google_api.get_book(phrase)

        Book.objects.create(
            title = book['title'],
            author = book['author'],
            published_date = self.convert_date(book['published']),
            isbn = book['isbn'],
            print_length = book['print_length'],
            cover = book['cover'],
            language = book['language']
        )
        return result


class BookUpdate(UpdateView):
    template_name = 'book_form.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books')
    context_object_name = 'book'


class BookDelete(DeleteView):
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('books')
    context_object_name = 'book'


class BooksApiView(APIView):
    def get(self, request, format='JSON'):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BooksApiView2(ListAPIView):
        serializer_class = BookSerializer
        def get_queryset(self):
            title = self.kwargs['title']
            return Book.objects.filter(title__icontains=title)
        
    
class BookApiView(APIView):
    def get_object(self, id):
        try:
            return Book.objects.get(id=id)

        except Book.DoesNotExist:
            raise Http404

    def get(self, request, id):
        book = self.get_object(id)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AboutMe(TemplateView):
    template_name = 'about_me.html'