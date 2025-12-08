from django.test import TestCase
from django.urls import reverse

class HomeViewTests(TestCase):
    def test_home_status_code(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_home_contains_title(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, '<h1>MySite</h1>')
