from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename = 'user')
router.register(r'experiments', views.ExperimentViewSet, basename = 'experiment')
router.register(r'results', views.ResultsViewSet, basename = 'results')

urlpatterns = [
    path('', include(router.urls)),
]