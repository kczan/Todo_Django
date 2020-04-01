from django.test import SimpleTestCase
from django.urls import reverse
from todo import urls as main_urls


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(url, '/register/')

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(url, '/profile/')

    def test_password_reset_url_is_resolved(self):
        url = reverse('password_reset')
        self.assertEqual(url, '/password-reset/')

    def test_password_reset_done_url_is_resolved(self):
        url = reverse('password_reset_done')
        self.assertEqual(url, '/password-reset/done/')

    def test_password_reset_confirm_url_is_resolved(self):
        url = reverse('password_reset_confirm', args=['Mjc', '5fa-5e3ae18112971ba48542'])
        self.assertEqual(url, '/password-reset-confirm/Mjc/5fa-5e3ae18112971ba48542/')

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse('password_reset_complete')
        self.assertEqual(url, '/password-reset-complete/')