from django.test import TestCase
from django.urls import reverse


class QuizTests(TestCase):
    def test_quiz(self):
        url = reverse('quiz:index')
        response = self.client.get(url)

        self.assertContains(response, "Enter capital for country:")
        self.assertEqual(response.status_code, 200)
