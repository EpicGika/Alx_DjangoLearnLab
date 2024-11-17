from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import book



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
