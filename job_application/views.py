from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializer, JobSerializer, SkillSerializer
from .models import (
    Job,Skill,Application
)
# Create your views here.

class JobViewsets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class SkillViewSets(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ApplicationViewSets(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer