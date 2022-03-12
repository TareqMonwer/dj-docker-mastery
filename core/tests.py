from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

from core.views import HomePageView


class HomePageViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response(self):
        url = reverse_lazy('core:homepage_url')
        response = self.client.get(url)

        self.assertEqual(response.resolver_match.func.__name__, HomePageView.as_view().__name__)
        self.assertURLEqual(url, '/', msg_prefix='Homepage URL')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('homepage' in str(response.content).lower())
        self.assertTemplateUsed(response, 'index.html')
