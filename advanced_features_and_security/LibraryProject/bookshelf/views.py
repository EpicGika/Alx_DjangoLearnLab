from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q
from .forms import SearchForm

# Permissions enforced using @permission_required decorator

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    book = get_object_or_404(book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Logic to create an book
        return redirect('book_list')
    return render(request, 'book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        # Logic to edit the book
        return redirect('book_detail', pk=book.pk)
    return render(request, 'book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(book, pk=pk)
    book.delete()
    return redirect('book_list')

# Secure Search Books View
def search_books(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['query']
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
        return render(request, 'books/book_list.html', {'books': books})
    else:
        # Handle form errors
        return render(request, 'books/book_list.html', {'form': form})