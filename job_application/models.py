from django.db import models
from users.models import CustomUser
# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "skills"

class Job(models.Model):
    title = models.TextField()
    description = models.TextField()
    employer = models.ForeignKey(CustomUser,related_name="jobs",on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=30)
    salary = models.FloatField()

    class Meta:
        db_table = "jobs"

class Application(models.Model):
    seeker = models.ManyToManyField(CustomUser)
    job = models.ForeignKey(Job,related_name="applications",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "applications"
