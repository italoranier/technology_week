from django.urls import path
from . import views

urlpatterns = [
    path('', views.technology_week, name='technology_week'),
]