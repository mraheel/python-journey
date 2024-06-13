from .models import Role, Permission, RolePermission
from .serializers import RoleSerializer, PermissionSerializer, AssignPermissionsSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class RoleListCreate(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionList(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class AssignPermissionToRole(APIView):
    # permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        request_body=AssignPermissionsSerializer,
        operation_id="assign_permissions_to_role",
        operation_description="Assign permissions to a role."
    )
    @transaction.atomic
    def post(self, request, role_id):
        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return Response({"error": "Role not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AssignPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            permission_ids = serializer.validated_data['permission_ids']
            permissions = Permission.objects.filter(id__in=permission_ids)
            
            # Clear existing permissions
            RolePermission.objects.filter(role=role).delete()
            
            # Add new permissions
            for permission in permissions:
                RolePermission.objects.create(role=role, permission=permission)
                
            return Response({"message": "Permissions assigned successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
