from django.db import models
from users.models import CustomUser
# Create your models here.
from users.models import CustomUser
# Create your models here.
class Job(models.Model):
    title = models.TextField()
    description = models.TextField()
    employer = models.ForeignKey(CustomUser,related_name="jobs",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=30)
    salary = models.FloatField()

    class Meta:
        db_table = "jobs"

class Skill(models.Model):
    name = models.CharField(max_length=30)
    job = models.ManyToManyField(Job)
    user = models.ManyToManyField(CustomUser)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "skills"

class Application(models.Model):
    seeker = models.ManyToManyField(CustomUser)
    job = models.ForeignKey(Job,related_name="applications",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "applications"
