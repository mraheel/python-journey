from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.RoleList.as_view(), name='Role_list'),

    # for web views
    # path('roles/', views.roles, name='roles'),
    # path('permissions/', views.permissions, name='permissions'),
]