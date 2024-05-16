from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from events.models import Event
from events.serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from utils.util import response_formattor

class EventList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful response"),
            400: openapi.Response("Error response")
        }
    )    
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        response_data = response_formattor(serializer.data, True, 'Data fetched successfully.')
        return Response(response_data, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(
        request_body=EventSerializer,
        responses={
            200: openapi.Response("Successful response"),
            400: openapi.Response("Error response")
        }
    )
    @transaction.atomic
    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EventDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EventSerializer(snippet)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=EventSerializer,
        responses={
            200: openapi.Response("Successful response"),
            400: openapi.Response("Error response")
        }
    )
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EventSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)