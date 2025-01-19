from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileViewsTests(APITestCase):
    def setUp(self):
        # Create user and let the signal create the Profile
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_user_login(self):
        # Test if the user can log in
        self.assertTrue(
            self.client.login(username='testuser', password='testpassword')
        )

    def test_profile_created(self):
        # Test if the profile is created when the user is created
        profile_exists = Profile.objects.filter(owner=self.user).exists()
        self.assertTrue(profile_exists, "The profile was not created.")
