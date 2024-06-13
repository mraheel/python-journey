from django.shortcuts import render

from .serializers import UserSerializer, AssignRoleSerializer
from .models import UserData, UserRole
from acl.models import Role
from acl.serializers import RoleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            200: openapi.Response("Successful response"),
            400: openapi.Response("Error response")
        }
    )
    @transaction.atomic
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class AssignUserRoleList(APIView):
    # permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_description="Get roles assigned to a user."
    )
    @transaction.atomic
    def get(self, request, user_id):
        try:
            user = UserData.objects.get(id=user_id)
        except UserData.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        roles = Role.objects.filter(userrole__user=user)
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=AssignRoleSerializer,
        operation_id="assign_role_to_user",
        operation_description="Assign a role to a user."
    )
    @transaction.atomic
    def post(self, request, user_id):
        try:
            user = UserData.objects.get(id=user_id)
        except UserData.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AssignRoleSerializer(data=request.data)
        if serializer.is_valid():
            role_id = serializer.validated_data['role_id']
            try:
                role = Role.objects.get(id=role_id)
                UserRole.objects.get_or_create(user=user, role=role)
                return Response({"message": "Role assigned successfully."}, status=status.HTTP_200_OK)
            except Role.DoesNotExist:
                return Response({"error": "Role not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)