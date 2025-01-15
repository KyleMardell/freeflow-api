from rest_framework import generics, permissions, filters
from freeflow_api.permissions import IsOwner
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    """
    List projects or create a project
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'status',
        'due_date'
    ]
    search_fields = [
        'title',
        'brief',
    ]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner]
    
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)