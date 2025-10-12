from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import (
    UserSerializer,CustomTokenObtainPairSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer