from django.shortcuts import render

from webapp.models import Book
from webapp.forms import BookForm
# from webapp.models import status_choices
from django.shortcuts import render, get_object_or_404, redirect


def book_index(request, *args, **kwargs):
    books = Book.objects.all()
    return render(request, 'index.html', context={
        'books': books
    })


def book_create(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book.objects.create(author=data['author'], email=data['email'], text=data['text'])
            return redirect('book_index')
        else:
            return render(request, 'create.html', context={'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(data={'author': book.author, 'email': book.email, 'text': book.text})
        return render(request, 'update.html', context={'form': form, 'book': book})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book.author = data['author']
            book.email = data['email']
            book.text = data['text']
            book.save()
            return redirect('book_index')
        else:
            return render(request, 'update.html', context={'form': form, 'book': book})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')
# Create your views here.
