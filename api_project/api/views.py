from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize data


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Require authentication
