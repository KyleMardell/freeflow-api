from rest_framework import serializers
from custom_tasks.models import CustomTask

class CustomTaskSerializer(serializers.ModelSerializer):
    """
    Custom task serializer.
    Owner as read only field.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    
    class Meta:
        model = CustomTask
        fields = [
            'id', 'owner', 'title', 'description',
            'estimated_time', 'average_time',
            'quickest_time', 'longest_time',
            'frequency', 'created_at', 'updated_at',
        ]