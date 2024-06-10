from django.urls import path, include
from rest_framework import routers
from . import views



urlpatterns = [
    path('clinics/', views.allClinics),
    path('clinique/<int:id>/', views.getClinic),
    path('addClinic/', views.addClinic),
    path('update/<int:id>/', views.updateClinic),
    path('delete/<int:id>/', views.delClinic),
]


