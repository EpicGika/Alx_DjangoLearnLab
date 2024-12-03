from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),  # Create Comment URL
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),  # Edit Comment URL
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),  # Delete Comment URL
    path('search/', views.search, name='search'),  # Search URL
    path('tags/<str:tag_name>/', views.tag_posts, name='tag_posts'),  # Tagging URL
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]