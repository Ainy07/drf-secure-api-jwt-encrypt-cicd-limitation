# api/tests.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import SecureData

class SecureDataAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.auth_header = f'Bearer {self.token}'
        self.url = reverse('secure-data')  

    def test_create_encrypted_data(self):
        data = {"plain_text": "Hello, secure world!"}
        response = self.client.post(
            "/api/secure-data/",
            data,
            format='json',
            HTTP_AUTHORIZATION=self.auth_header
        )
        print(response.json() , "RESPONSE")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("decrypted_text", response.data)
