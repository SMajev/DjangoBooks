import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
            'published_date': ['icontains'],
            'isbn': ['icontains'],
            'print_length': ['icontains'],
            'language': ['icontains'],
        }