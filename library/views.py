from django.shortcuts import render
from library.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(req):
    return render(req, 'library/index.html')
@login_required    
def show(req):
    context = { 'books' : Book.objects.all() }
    return render(req, 'library/all-books.html',context)
@login_required
def showbyid(req,id):
    context = { 'books' : Book.objects.filter(id=id) }
    return render(req, 'library/book.html', context)
