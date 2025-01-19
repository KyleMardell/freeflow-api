from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    User profile serializer.
    Owner as read only field.
    Email as email field, required set to false to allow null values.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.EmailField(required=False)

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'bio',
            'email', 'phone',
            'image', 'created_at', 'updated_at',
        ]
