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



