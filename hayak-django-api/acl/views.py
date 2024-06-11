from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Role, Permission
from .serializers import RoleSerializer

from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from utils.util import response_formattor

class RoleList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful response"),
            400: openapi.Response("Error response")
        }
    )    
    def get(self, request, format=None):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        response_data = response_formattor(serializer.data, True, 'Data fetched successfully.')
        return Response(response_data, status=status.HTTP_200_OK)
    

    # @swagger_auto_schema(
    #     request_body=EventSerializer,
    #     responses={
    #         200: openapi.Response("Successful response"),
    #         400: openapi.Response("Error response")
    #     }
    # )
    # @transaction.atomic
    # def post(self, request, format=None):
    #     serializer = EventSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for web
# def roles(request):
#     roles = Role.objects.all().values()
#     template = loader.get_template('roles/index.html')
#     context = {
#         'roles': roles,
#     }
#     return HttpResponse(template.render(context, request))

def permissions(request):
    permissions = Permission.objects.all().values()
    template = loader.get_template('permissions/index.html')
    context = {
        'permissions': permissions,
    }
    return HttpResponse(template.render(context, request))
