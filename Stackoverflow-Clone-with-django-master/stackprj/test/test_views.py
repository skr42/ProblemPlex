# problemplex/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from stackbase.models import Question
from django.contrib.auth import get_user_model

class QuestionViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.question = Question.objects.create(title="Test Question", content="Content", author=self.user)

    def test_question_list_view(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'problemplex/question_list.html')

    def test_question_detail_view(self):
        response = self.client.get(reverse('question_detail', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'problemplex/question_detail.html')
