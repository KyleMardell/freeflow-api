from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    email = serializers.EmailField(required=False)

    def get_is_owner(self, obj):
        """
        Check if the logged-in user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'bio',
            'email', 'phone',
            'image', 'created_at', 'updated_at',
            'is_owner',
        ]