from django.urls import path
from . import views

urlpatterns = [
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library-detail'),
]
