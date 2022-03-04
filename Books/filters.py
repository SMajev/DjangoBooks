import django_filters as df
from .models import Book



class BookFilter(df.FilterSet):

    CHOICES = (
        ('title', 'Title +'),
        ('-title', 'Title -'),
        ('author', 'Author +'),
        ('-author', 'Author -'),
        ('published_date', 'Published +'),
        ('-published_date', 'Published -')
    )
    ordering = df.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
            'language': ['icontains'],
            'published_date': ['gt', 'lt']
        }

    def filter_by_ordering(self, queryset, name, value):
        return queryset.order_by(value)
     