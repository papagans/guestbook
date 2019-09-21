from django.shortcuts import render

from webapp.models import Book
from webapp.forms import BookForm
# from webapp.models import status_choices
from django.shortcuts import render, get_object_or_404, redirect


def book_index(request, *args, **kwargs):
    books = Book.objects.exclude(status='blocked').order_by('-created_at')
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


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('book_index')


def book_search(request):
    search = request.GET.get('search')
    books = Book.objects.filter(author__contains=search)
    return render(request, 'search.html', context={
        'books': books
    })
# Create your views here.
