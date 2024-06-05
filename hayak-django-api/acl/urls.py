from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.roles, name='roles'),
    path('permissions/', views.permissions, name='permissions'),
]