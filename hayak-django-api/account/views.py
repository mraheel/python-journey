from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response

from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# view for registering users
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