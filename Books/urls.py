from django.urls import path
from .views import BooksView, BookCreate, BookImport


urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('addbook', BookCreate.as_view(), name='add-book'),
    path('importbook', BookImport.as_view(), name='book-import')
]
