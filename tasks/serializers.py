from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id', 'custom_task', 'title',
            'description', 'estimated_time', 
            'actual_time', 'due_date', 'status',
            'created_at', 'updated_at',
        ]