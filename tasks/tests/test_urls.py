from django.test import SimpleTestCase
from django.urls import reverse


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEqual(url, '/list/')

    def test_update_url_is_resolved(self):
        url = reverse('update_task', args=[1])
        self.assertEqual(url, '/list/update_task/1/')

    def test_delete_url_is_resolved(self):
        url = reverse('delete_task', args=[1])
        self.assertEqual(url, '/list/delete_task/1/')
