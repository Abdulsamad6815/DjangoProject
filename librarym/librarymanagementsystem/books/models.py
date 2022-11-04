from django.db import models

# Create your models here.
class Library(models.Model):
    book_name =models.CharField(max_length=20)
    author_name =models.CharField(max_length=20)
    price=models.IntegerField()

    type_of_book=models.CharField(max_length=20,default='')
    is_deleted=models.CharField(max_length=2,default='n')
