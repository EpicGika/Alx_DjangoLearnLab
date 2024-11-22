from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Retain the existing BookList view for listing books
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs
    path('', include(router.urls)),  # Automatically adds CRUD routes for BookViewSet

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
