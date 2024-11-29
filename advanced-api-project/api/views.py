from django.shortcuts import render
from rest_framework import generics, permissions, status, filters
from .models import Book
from .serializers import BookSerializer

# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__name', 'title']  # Example of filtering by author or title
    permission_classes = [permissions.AllowAny]  # Read-only access for everyone

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for everyone

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Book created successfully!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Book updated successfully!", "data": serializer.data})

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete


# BookListView: Handles retrieval of all books. Allows unauthenticated access.
# BookDetailView: Handles retrieval of a specific book by ID. Allows unauthenticated access.
# BookCreateView: Handles creation of new books. Restricted to authenticated users.
# BookUpdateView: Handles updates to existing books. Restricted to authenticated users.
# BookDeleteView: Handles deletion of books. Restricted to authenticated users.
