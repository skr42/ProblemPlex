from django.test import TestCase
from django.urls import reverse
from stackbase.models import User, Question, Answer

class UserAuthTests(TestCase):
    def test_register_user_with_valid_data(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_with_correct_credentials(self):
        User.objects.create_user(username='testuser', password='password123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_with_incorrect_credentials(self):
        User.objects.create_user(username='testuser', password='password123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')

    def test_logout_user(self):
        User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

class QuestionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_create_question(self):
        response = self.client.post(reverse('create_question'), {
            'title': 'How to test in Django?',
            'body': 'I need help with testing in Django.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Question.objects.filter(title='How to test in Django?').exists())

    def test_edit_question(self):
        question = Question.objects.create(title='Test question', body='Body', author=self.user)
        response = self.client.post(reverse('edit_question', args=[question.id]), {
            'title': 'Updated question title',
            'body': 'Updated body'
        })
        question.refresh_from_db()
        self.assertEqual(question.title, 'Updated question title')

    def test_delete_question(self):
        question = Question.objects.create(title='Test question', body='Body', author=self.user)
        response = self.client.post(reverse('delete_question', args=[question.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Question.objects.filter(id=question.id).exists())

class AnswerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        self.question = Question.objects.create(title='Sample Question', body='Question body', author=self.user)

    def test_post_answer(self):
        response = self.client.post(reverse('post_answer', args=[self.question.id]), {
            'body': 'This is an answer.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Answer.objects.filter(body='This is an answer.').exists())

    def test_upvote_answer(self):
        answer = Answer.objects.create(body='Answer body', question=self.question, author=self.user)
        response = self.client.post(reverse('upvote_answer', args=[answer.id]))
        answer.refresh_from_db()
        self.assertEqual(answer.upvotes, 1)

    def test_multiple_votes_on_same_answer(self):
        answer = Answer.objects.create(body='Answer body', question=self.question, author=self.user)
        self.client.post(reverse('upvote_answer', args=[answer.id]))
        response = self.client.post(reverse('upvote_answer', args=[answer.id]))
        answer.refresh_from_db()
        self.assertEqual(answer.upvotes, 1)
