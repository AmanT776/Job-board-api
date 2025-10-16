from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializer, JobSerializer, SkillSerializer
from .models import (
    Job,Skill,Application
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
# Create your views here.

class JobViewsets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def list(self,request,*args,**kwargs):
        queryset = Job.objects.all()
        jobs = []
        for job in queryset:
            skills = [skill.name for skill in job.skill.all()]
            jobs.append({
                "title": job.title,
                "description": job.description,
                "skill": skills,
                "employer": job.employer.first_name + " " + job.employer.last_name,
                "location": job.location
            })
        return Response(
            {
                "success": True,
                "message": "jobs successfully retrieved",
                "count": len(jobs),
                "jobs": jobs
            }
        )
        
class SkillViewSets(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class ApplicationViewSets(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]