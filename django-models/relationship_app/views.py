from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import render
from .models import Book


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'