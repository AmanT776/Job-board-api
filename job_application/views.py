from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JobSerializer
from .models import (
    Job
)
# Create your views here.

class JobViewsets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
