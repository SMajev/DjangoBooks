from django.db import models
from datetime import datetime as dt


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, null=True)
    print_length = models.IntegerField(null=True)
    cover = models.URLField(null=True)
    language = models.CharField(max_length=60)



