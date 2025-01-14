from rest_framework import serializers
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate_hourly_rate(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Hourly rate cannot be a negative number.")
        return value
    
    class Meta:
        model = Project
        fields = [
            'id', 'owner', 'title', 'brief',
            'hourly_rate', 'status', 'due_date',
            'created_at', 'updated_at',
        ]