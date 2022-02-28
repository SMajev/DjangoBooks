from django.contrib import admin
from .models import Book

@admin.register(Book)
class AdminBooks(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'published_date', 'isbn',
        'print_length', 'cover', 'language'
    )
