from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    print_length = models.IntegerField()
    cover = models.URLField()
    language = models.CharField(max_length=60)
