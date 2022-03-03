from django.urls import path
from .views import (
    BooksView, BookCreate, BookImport, BookUpdate,
    BookDelete, BookDetailView
)


urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('<int:pk>', BookDetailView.as_view(), name='book'),
    path('addbook', BookCreate.as_view(), name='add-book'),
    path('importbook', BookImport.as_view(), name='import-book'),
    path('updatebook/<int:pk>', BookUpdate.as_view(), name='update-book'),
    path('deletebook/<int:pk>', BookDelete.as_view(), name='delete-book')
]
