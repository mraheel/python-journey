from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.RoleListCreate.as_view(), name='role-list-create'),
    path('permissions/', views.PermissionList.as_view(), name='permission-list'),
    path('roles/<int:role_id>/permissions', views.AssignPermissionToRole.as_view(), name='assign-permission-to-role'),
]