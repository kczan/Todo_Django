from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from todo import views as main_views


class TestViews(TestCase):

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        resolver = resolve(reverse('home'))
        self.assertEqual(resolver.view_name, 'home')
        self.assertTemplateUsed(response, 'main_home.html')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/login/?next=/profile/', status_code=302, target_status_code=200,
                             fetch_redirect_response=False)

    def test_password_reset_view(self):
        response = self.client.get(reverse('password_reset'))
        resolver = resolve(reverse('password_reset'))
        self.assertEqual(resolver.view_name, 'password_reset')
        self.assertTemplateUsed(response, 'users/password_reset.html')

    def test_password_reset_done_view(self):
        response = self.client.get(reverse('password_reset_done'))
        resolver = resolve(reverse('password_reset_done'))
        self.assertEqual(resolver.view_name, 'password_reset_done')
        self.assertTemplateUsed(response, 'users/password_reset_done.html')

    def test_password_reset_confirm_view(self):
        response = self.client.get(reverse('password_reset_confirm', args=['Mjc', '5fa-5e3ae18112971ba48542']))
        resolver = resolve(reverse('password_reset_confirm', args=['Mjc', '5fa-5e3ae18112971ba48542']))
        self.assertEqual(resolver.view_name, 'password_reset_confirm')
        self.assertTemplateUsed(response, 'users/password_reset_confirm.html')

    def test_password_reset_complete_view(self):
        response = self.client.get(reverse('password_reset_complete'))
        resolver = resolve(reverse('password_reset_complete'))
        self.assertEqual(resolver.view_name, 'password_reset_complete')
        self.assertTemplateUsed(response, 'users/password_reset_complete.html')


class LoggedInTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')


class TestLoggedInViews(LoggedInTestCase):

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('list'), status_code=302, target_status_code=200, fetch_redirect_response=False)

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=False)

    def test_if_user_logged_in(self):
        user = auth.get_user(self.client)
        assert user.is_authenticated

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        resolver = resolve(reverse('profile'))
        self.assertEqual(resolver.view_name, 'profile')
        self.assertTemplateUsed(response, 'users/profile.html')




