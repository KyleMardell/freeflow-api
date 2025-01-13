from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.EmailField(required=False)


    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'bio',
            'email', 'phone',
            'image', 'created_at', 'updated_at',
        ]