from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# Registration View


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login after successful registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
