from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from django.contrib import auth


class LoggedInTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')


class TestLoggedInViews(LoggedInTestCase):

    def test_login_view(self):
        client = Client()
        response = client.get(reverse('login'))
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_register_view(self):
        client = Client()
        response = client.get(reverse('register'))
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_if_user_logged_in(self):
        user = auth.get_user(self.client)
        assert user.is_authenticated



