from rest_framework import generics, permissions, filters
from freeflow_api.permissions import IsProjectOwner
from .models import Task, Project
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    """
    Lists tasks or create a task only if you're the owner.
    Search by title or description
    Order by due date, status or estimated time.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        'title',
        'description',
    ]
    ordering_fields = [
        'due_date',
        'estimated_time',
        'status',
    ]

    def get_queryset(self):
        project = self.kwargs['project_id']
        return Task.objects.filter(project=project)

    def perform_create(self, serializer):
        """
        Adds the project id from the URL args as the
        tasks project id.
        """
        project = self.kwargs['project_id']
        project_instance = Project.objects.get(id=project)
        serializer.save(project=project_instance)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve edit or delete a task
    only if you're the owner.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsProjectOwner]
    
    def get_queryset(self):
        project = self.kwargs['project_id']
        return Task.objects.filter(project=project)