# problemplex/tests/test_models.py
from django.test import TestCase
from stackbase.models import Question, Answer
from django.contrib.auth import get_user_model

class QuestionModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.question = Question.objects.create(title="Test Question", content="Question content", author=self.user)

    def test_question_creation(self):
        self.assertEqual(self.question.title, "Test Question")
        self.assertEqual(self.question.author.username, "testuser")

    def test_question_string_representation(self):
        self.assertEqual(str(self.question), self.question.title)

class AnswerModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(title="Another Test Question", content="Content", author=self.user)
        self.answer = Answer.objects.create(content="Test Answer", question=self.question, author=self.user)

    def test_answer_creation(self):
        self.assertEqual(self.answer.content, "Test Answer")
        self.assertEqual(self.answer.question, self.question)
