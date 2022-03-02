from django.urls import path
from .views import BooksView, BookCreate, BookImport, BookUpdate


urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('addbook', BookCreate.as_view(), name='add-book'),
    path('importbook', BookImport.as_view(), name='import-book'),
    path('updatebook/<int:pk>', BookUpdate.as_view(), name='update-book')
]
