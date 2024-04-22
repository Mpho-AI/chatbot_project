from django.test import TestCase
from django.urls import reverse
from.views import chatbot_response
from django.http import JsonResponse

class ChatbotTestCase(TestCase):
    def test_chatbot_response(self):
        url = reverse('chatbot_response')
        response = self.client.get(url, {'input': 'What is the poverty rate in Brazil?'})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertIn('response', response.json())

    def test_chatbot_response_error(self):
        url = reverse('chatbot_response')
        response = self.client.get(url, {'input': ''})
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, JsonResponse)
        self.assertIn('error', response.json())