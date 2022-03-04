from django.urls import path
from .views import (
    BooksView, BookCreate, BookImport, BookUpdate,
    BookDelete, BookDetailView, BooksApiView, BookApiView,
    BooksApiView2, AboutMe
)


urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('aboutme', AboutMe.as_view(), name='about-me'),
    path('<int:pk>', BookDetailView.as_view(), name='book'),
    path('addbook', BookCreate.as_view(), name='add-book'),
    path('importbook', BookImport.as_view(), name='import-book'),
    path('updatebook/<int:pk>', BookUpdate.as_view(), name='update-book'),
    path('deletebook/<int:pk>', BookDelete.as_view(), name='delete-book'),
    path('api/books', BooksApiView.as_view(), name='api-books'),
    path('api/books/<title>', BooksApiView2.as_view(), name='api-books2'),
    path('api/books/<int:id>', BookApiView.as_view(), name='api-book')
]
