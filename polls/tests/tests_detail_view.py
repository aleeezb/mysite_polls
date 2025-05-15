from polls.tests.halper import create_question
from django.test import TestCase
from django.urls import reverse


class TestQuestionDetailView(TestCase):
    def test_detail_view_raises_404_for_future_question(self):
        q = create_question(text="sample",days=10)
        response = self.client.get(reverse("polls:detail",args=(q.id, )))
        self.assertEqual(response.status_code, 404)
    
    def test_detail_view_shows_past_question(self):
        q = create_question(text="sample",days=-10)
        response = self.client.get(reverse("polls:detail",args=(q.id, )))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,f"Question: {q.question_text}")