from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Project serializers
    OWner as read only field
    Adds natural time to updated at
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    updated_at = serializers.SerializerMethodField()

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate_hourly_rate(self, value):
        """
        Checks the hourly rate is a positive number
        """
        if value is not None and value < 0:
            raise serializers.ValidationError(
                "Hourly rate cannot be a negative number."
            )
        return value

    class Meta:
        model = Project
        fields = [
            'id', 'owner', 'title', 'brief',
            'hourly_rate', 'status', 'due_date',
            'created_at', 'updated_at',
        ]
