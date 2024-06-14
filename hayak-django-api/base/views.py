from django.db import transaction

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import SystemSetting, Country, State, City, Language, Timezone
from .serializers import SystemSettingSerializer, UpdateSystemSettingSerializer, CountrySerializer, StateSerializer, CitySerializer, LanguageSerializer, TimezoneSerializer
    
class SystemSettings(APIView):
    # permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_description="Get system-wide settings."
    )
    @transaction.atomic
    def get(self, request):
        settings = SystemSetting.objects.all()
        serializer = SystemSettingSerializer(settings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UpdateSystemSettingSerializer,
        operation_id="update_system_settings",
        operation_description="Update settings for a specific user."
    )
    @transaction.atomic
    def put(self, request):
        serializer = UpdateSystemSettingSerializer(data=request.data)
        if serializer.is_valid():
            settings = serializer.validated_data['settings']
            for key, value in settings.items():
                SystemSetting.objects.update_or_create(
                    key=key,
                    defaults={'value': value}
                )
            return Response({"message": "Settings updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateListByCountry(APIView):
    @swagger_auto_schema(
        manual_parameters = [
            openapi.Parameter(
                'country_id',
                openapi.IN_QUERY,
                description="Id of the country for which to retrieve the states",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={200: StateSerializer(many=True)}
    )
    def get(self, request, format=None):
        country_id = request.query_params.get('country_id')
        if country_id is None:
            return Response({'error': 'country_id query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        states = State.objects.filter(country_id=country_id)
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

class CityListByState(APIView):
    @swagger_auto_schema(
        manual_parameters = [
            openapi.Parameter(
                'state_id',
                openapi.IN_QUERY,
                description="Id of the state for which to retrieve the cities",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        responses={200: CitySerializer(many=True)}
    )
    def get(self, request, format=None):
        state_id = request.query_params.get('state_id')
        if state_id is None:
            return Response({'error': 'state_id query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        cities = City.objects.filter(state_id=state_id)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    
class LanguageList(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class TimezoneList(generics.ListAPIView):
    queryset = Timezone.objects.all()
    serializer_class = TimezoneSerializer