from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import Task


class TestNotLoggedInViews(TestCase):

    def test_list_view(self):
        client = Client()
        response = client.get(reverse('list'))
        self.assertEqual(response.status_code, 302)

    def test_update_view(self):
        client = Client()
        response = client.get(reverse('update_task', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):
        client = Client()
        response = client.get(reverse('delete_task', args=[1]))
        self.assertEqual(response.status_code, 302)


class LoggedInTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        Task.objects.create(title='test')  # creating a task of id 1 (first on the list) to test update and delete functionality


class TestLoggedInViews(LoggedInTestCase):

    def test_if_user_logged_in(self):
        user = auth.get_user(self.client)
        assert user.is_authenticated

    def test_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/list.html')

    def test_update_view(self):
        response = self.client.get(reverse('update_task', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/update_task.html')

    def test_delete_view(self):
        response = self.client.get(reverse('delete_task', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/delete_task.html')
