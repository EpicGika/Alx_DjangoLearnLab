# accounts/views.py
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, LoginSerializer
from rest_framework.authtoken.models import Token

class UserRegistrationView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registered successfully",
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.create(serializer.validated_data)
            return Response({"token": token['token']}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
