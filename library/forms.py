from django import forms
from library.models import Book
from django.forms import ModelForm

class NewBookForm(ModelForm):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)

    class Meta:
        model = Book
        fields = ['title','author']

class BorrowBookForm(ModelForm):
    class Meta:
        fields = ['borrower']
        model = Book
        
    