from django.db.models import Count
from rest_framework import generics, permissions, filters
from freeflow_api.permissions import IsOwner
from .models import CustomTask
from .serializers import CustomTaskSerializer


class CustomTaskList(generics.ListCreateAPIView):
    """
    Lists custom tasks or create a custom task

    """
    serializer_class = CustomTaskSerializer
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
        'frequency',
        'average_time',
        'estimated_time',
    ]

    def get_queryset(self):
        return CustomTask.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CustomTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomTaskSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return CustomTask.objects.filter(owner=self.request.user)