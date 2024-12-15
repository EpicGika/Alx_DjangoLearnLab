from rest_framework import viewsets, permissions, generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'content']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Get the Post object or return 404 if not found
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Use get_or_create to ensure a user can't like a post more than once
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            # If the like already exists, return a response indicating so
            return Response({"detail": "You have already liked this post."}, status=400)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

        return Response({"detail": "Post liked successfully."}, status=201)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Get the Post object or return 404 if not found
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Try to get the Like object for the user and post
        like = Like.objects.get_or_create(user=request.user, post=post).first()

        if not like:
            # If the like doesn't exist, return a response indicating so
            return Response({"detail": "You have not liked this post."}, status=400)

        like.delete()  # Remove the like

        return Response({"detail": "Post unliked successfully."}, status=200)
