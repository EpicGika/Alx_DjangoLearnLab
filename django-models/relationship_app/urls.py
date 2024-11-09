from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library-detail'),
]
