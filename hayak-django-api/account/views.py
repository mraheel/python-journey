from django.db import transaction

from .models import UserData, UserRole, UserSetting
from .serializers import UserSerializer, AssignRoleSerializer, UserSettingSerializer, UpdateUserSettingSerializer
from acl.models import Role
from acl.serializers import RoleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
    
class UserSettings(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get settings for a specific user."
    )
    @transaction.atomic
    def get(self, request, user_id):
        try:
            user = UserData.objects.get(id=user_id)
        except UserData.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != user:
            return Response({"error": "You do not have permission to view these settings."}, status=status.HTTP_403_FORBIDDEN)

        settings = UserSetting.objects.filter(user=user)
        serializer = UserSettingSerializer(settings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UpdateUserSettingSerializer,
        operation_id="update_user_settings",
        operation_description="Update settings for a specific user."
    )
    @transaction.atomic
    def put(self, request, user_id):
        try:
            user = UserData.objects.get(id=user_id)
        except UserData.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != user:
            return Response({"error": "You do not have permission to update these settings."}, status=status.HTTP_403_FORBIDDEN)

        serializer = UpdateUserSettingSerializer(data=request.data)
        if serializer.is_valid():
            settings = serializer.validated_data['settings']
            for key, value in settings.items():
                UserSetting.objects.update_or_create(
                    user=user,
                    key=key,
                    defaults={'value': value}
                )
            return Response({"message": "Settings updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)