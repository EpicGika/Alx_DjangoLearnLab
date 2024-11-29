from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filtering, searching, and ordering capabilities
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Define fields for filtering
    filterset_fields = ['author__name', 'title', 'publication_year']

    # Define fields for searching
    search_fields = ['title', 'author__name']

    # Define fields for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
    
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

# BookListView: Handles retrieval of all books. Allows unauthenticated access.
# BookDetailView: Handles retrieval of a specific book by ID. Allows unauthenticated access.
# BookCreateView: Handles creation of new books. Restricted to authenticated users.
# BookUpdateView: Handles updates to existing books. Restricted to authenticated users.
# BookDeleteView: Handles deletion of books. Restricted to authenticated users.
