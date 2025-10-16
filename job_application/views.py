from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializer, JobSerializer, SkillSerializer
from .models import (
    Job,Skill,Application
)

from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework import status
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

    def create(self, request, *args, **kwargs):
        if(self.request.user.role != "seeker"):
            return Response({
                "message": "only seekers can apply for a job",
            },status.HTTP_403_FORBIDDEN)
        job_id = request.data.get("job")
        if not job_id:
            return Response({
                "status": False,
                "message": "job id is required."
            },status.HTTP_400_BAD_REQUEST)
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({
                "success": False,
                "message": "Job not found",
            },status.HTTP_404_NOT_FOUND)
        if Application.objects.filter(seeker=self.request.user,job=job).exists():
            return Response({
                "success": False,
                "message": "Application already found"
            },status.HTTP_400_BAD_REQUEST)
        application = Application.objects.create(seeker=self.request.user,job=job)
        serializer = self.get_serializer(application)
        
        return Response({
            "success": True,
            "message": "you have successfully applied",
            "application": serializer.data
        },status.HTTP_200_OK)