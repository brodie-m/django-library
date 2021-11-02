from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    borrower = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)