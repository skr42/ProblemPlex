# problemplex/tests/test_api.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from stackbase.models import Question
from django.contrib.auth import get_user_model

class QuestionAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.question = Question.objects.create(title="Test API Question", content="Content", author=self.user)

    def test_question_list_api(self):
        response = self.client.get(reverse('api:question-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question_detail_api(self):
        url = reverse('api:question-detail', args=[self.question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.question.title)
