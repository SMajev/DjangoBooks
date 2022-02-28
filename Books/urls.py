from django.urls import path
from .views import BooksView, BookCreate


urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('addbook', BookCreate.as_view(), name='add-book')
]
