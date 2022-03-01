from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BookImportForm(forms.Form):
    class Meta:
        fields = '__all__'
    title = forms.CharField(label='title', max_length=128)