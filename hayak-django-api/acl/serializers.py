from rest_framework import serializers
from .models import Role, Permission


class RoleSerializer(serializers.ModelSerializer):
   class Meta:
        model = Role
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
   class Meta:
        model = Permission
        fields = '__all__'

class AssignPermissionsSerializer(serializers.Serializer):
    permission_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )

    def validate_permission_ids(self, value):
        if not Permission.objects.filter(id__in=value).exists():
            raise serializers.ValidationError("One or more permissions do not exist.")
        return value



