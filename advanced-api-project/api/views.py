from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    """
    API view for listing books with filtering, searching, and ordering.

    Features:
    - Filtering: Use query parameters like `?author__name=John+Doe` or `?publication_year=2022`.
    - Searching: Use `?search=Python` to perform a text search on the title or author name.
    - Ordering: Use `?ordering=title` or `?ordering=-publication_year` to sort results.

    Default ordering: By title in ascending order.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__name', 'title', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

# BookListView: Handles retrieval of all books. Allows unauthenticated access.
# BookDetailView: Handles retrieval of a specific book by ID. Allows unauthenticated access.
# BookCreateView: Handles creation of new books. Restricted to authenticated users.
# BookUpdateView: Handles updates to existing books. Restricted to authenticated users.
# BookDeleteView: Handles deletion of books. Restricted to authenticated users.
