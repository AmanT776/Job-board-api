from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSets, JobViewsets, SkillViewSets

router = DefaultRouter()
router.register(r'jobs',JobViewsets,basename='jobs')
router.register(r'skills',SkillViewSets,basename='skills')
router.register(r'apply',ApplicationViewSets,basename='apply')
urlpatterns = [
    path('',include(router.urls))
]