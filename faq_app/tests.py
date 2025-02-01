from django.test import TestCase
from rest_framework.test import APITestCase
from faq_app.models import FAQ

class FAQApiTest(APITestCase):
    
    def setUp(self):
        # Create some FAQ objects
        FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        FAQ.objects.create(question="What is Python?", answer="Python is a programming language.")
    
    def test_get_faqs_in_english(self):
        response = self.client.get('/api/faqs/?lang=en')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
    
    def test_get_faqs_in_hindi(self):
        # Assuming translations for Hindi exist
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

