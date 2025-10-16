from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import (
    UserSerializer,CustomTokenObtainPairSerializer,ProfileSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveAPIView
from .models import Profile
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        if not profile:
            return Response({
                "success": False,
                "message": "Profile not found"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(profile)
        return Response({
            "success": True,
            "message": "Profile retrieved successfully",
            "profile": serializer.data
        }, status=status.HTTP_200_OK)