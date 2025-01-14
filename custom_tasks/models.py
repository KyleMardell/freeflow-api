from django.db import models
from django.contrib.auth.models import User

class CustomTask(models.Model):
    """
    Custom task model, related to 'owner', i.e. a User instance
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)    
    estimated_time = models.DecimalField(max_digits=5, decimal_places=2)
    average_time = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    quickest_time = models.DecimalField(max_digits=5, decimal_places=2,  default=0.0)
    longest_time = models.DecimalField(max_digits=5, decimal_places=2,  default=0.0)
    frequency = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Custom task: {self.title}'