from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BookImportForm(forms.Form):
    phrase = forms.CharField(label='Phrase', max_length=128)
    class Meta:
        fields = '__all__'

class BookFromGoogle(forms.Form):
    class Meta:
        model = Book
        fields = '__all__'

    
