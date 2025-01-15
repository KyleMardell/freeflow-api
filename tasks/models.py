from django.db import models
from projects.models import Project
from custom_tasks.models import CustomTask


class Task(models.Model):
    """
    Task model, related to 'owner', i.e. a User instance, may also
    be related to 'custom_task' if used as an optional field.
    """
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('complete', 'Complete'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    custom_task = models.ForeignKey(CustomTask, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)    
    estimated_time = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    actual_time = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Task: {self.title}'