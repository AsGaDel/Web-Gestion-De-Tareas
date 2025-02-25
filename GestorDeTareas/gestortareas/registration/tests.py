from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'email@gmail.com', 'testpassword')

    def test_profile_exists(self):
        user_exists = Profile.objects.filter(user__username='test').exists()
        profile_exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(user_exists, True)
        self.assertEqual(profile_exists, True)

