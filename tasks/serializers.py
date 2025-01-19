from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Task serializer.
    Adds natural time to updated at
    """
    updated_at = serializers.SerializerMethodField()

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Task
        fields = [
            'id', 'custom_task', 'title',
            'description', 'estimated_time',
            'actual_time', 'due_date', 'status',
            'created_at', 'updated_at',
        ]
