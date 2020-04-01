from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse
from tasks.views import list_homepage, update_task, delete_task
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import Task


# class TestViews(SimpleTestCase):
#
#     def test_list(self):
#         resolver = resolve('/list/')
#         print(resolver)
#         self.assertEqual(resolver.func, list_homepage)
#
#     def test_update(self):
#         resolver = resolve('/list/update_task/')
#         print(resolver)
#         self.assertEqual(resolver.func, update_task)
#
#     def test_delete(self):
#         resolver = resolve('/list/delete_task/')
#         print(resolver)
#         self.assertEqual(resolver.func, delete_task)


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

