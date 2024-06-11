from rest_framework import serializers
from .models import Country, State, City, Language, Timezone

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = '__all__'
