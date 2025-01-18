from django.test import TestCase
from .factories import UserFactory
from django.test import Client
from django.urls import reverse
from app.models import User
from app.serializers import LoginSerializer


class TestAuthAPI(TestCase):
    def setUp(self) -> None:
        self.password = "dummypassword"
        self.email = "dummy@example.com"
        self.user = UserFactory.create(email=self.email, password=self.password)

    def test_valid_login(self):
        client = Client()
        response = client.post(
            reverse("login-api-list"),
            {
                "email": self.email,
                "password": self.password,
            },
            content_type="application/json",
        )
        response_data = response.json()

        self.assertEqual(200, response.status_code)
        self.assertTrue("token" in response_data)

        user = User.objects.get(email=self.email)
        self.assertTrue(user.check_password(self.password))

    def test_invalid_email_login(self):
        client = Client()
        response = client.post(
            reverse("login-api-list"),
            {
                "email": "fake@example.com",
                "password": self.password,
            },
            content_type="application/json",
        )
        response_data = response.json()

        self.assertEqual(400, response.status_code)
        self.assertEqual(LoginSerializer.INVALID_LOGIN, response_data["non_field_errors"][0])

    def test_invalid_password_login(self):
        client = Client()
        response = client.post(
            reverse("login-api-list"),
            {
                "email": self.email,
                "password": "invalid-password",
            },
            content_type="application/json",
        )
        response_data = response.json()
        self.assertEqual(400, response.status_code)
        self.assertEqual(LoginSerializer.INVALID_LOGIN, response_data["non_field_errors"][0])
