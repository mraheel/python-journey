from rest_framework import serializers
from events.models import Event, Category, Template


class EventSerializer(serializers.ModelSerializer):
   class Meta:
        model = Event
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    templates = TemplateSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'is_active', 'templates']

class EventStep1Serializer(serializers.ModelSerializer):
   class Meta:
        model = Event
        fields = ['name', 'type', 'description', 'guests', 'tbd', 'start_date', 'start_time', 'end_time', 'address', 'latitude', 'longitude']
        extra_kwargs = {
            'description': {'required': False},
            'guests': {'required': False},
            'tbd': {'required': False},
            'start_date': {'required': False},
            'start_time': {'required': False},
            'end_time': {'required': False},
            'address': {'required': False},
            'latitude': {'required': False},
            'longitude': {'required': False},
        }

        def create(self, validated_data):
            user = self.context['request'].user
            return Event.objects.create(user=user, **validated_data)


