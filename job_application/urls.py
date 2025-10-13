from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    JobViewsets,SkillViewSets
)

router = DefaultRouter()
router.register(r'jobs',JobViewsets,basename='jobs')
router.register(r'skills',SkillViewSets,basename='skills')

urlpatterns = [
    path('',include(router.urls))
]