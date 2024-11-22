from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize data


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    (list, create, retrieve, update, destroy) for the Book model.
    """
    queryset = Book.objects.all()  # Query all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for data serialization
