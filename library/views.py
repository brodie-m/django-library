from django.shortcuts import redirect, render
from library.forms import BorrowBookForm, NewBookForm
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
    book_to_save = Book.objects.get(id=id)
    if req.method == 'POST':
        form = BorrowBookForm(req.POST)
        
        if form.is_valid() and not book_to_save.borrower:
            book_to_save.borrower = form.cleaned_data['borrower']
            book_to_save.save()
            return redirect('books-show')
        else:
            book_to_save.borrower = None
            book_to_save.save()
    else:
        form = BorrowBookForm()
    data = {'form': form, 'books' : Book.objects.filter(id=id), 'book_to_save':book_to_save}
    
    return render(req, 'library/book.html', data)
def new_book(req):
    if req.method == 'POST':
        form = NewBookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('books-show')
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(req, 'library/new-book.html', data)
