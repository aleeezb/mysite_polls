from django.test import TestCase
from django.urls import reverse
from polls.models import Question, Choice
from django.utils import timezone
import datetime


# Helper function
def create_question(text, days):
    question = Question.objects.create(
        question_text=text,
        pub_date=timezone.now() + datetime.timedelta(days=days)
    )
    return question

def create_question_with_choice(text, days):
    question = create_question(text, days)
    question.choice_set.create(choice_text="Option 1", votes=0)
    return question


class TestQuestionResultsView(TestCase):
    def test_results_view_raises_404_for_future_question(self):
        q = create_question("Future Question", days=10)
        url = reverse("polls:results", args=(q.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_results_view_shows_past_question(self):
        q = create_question_with_choice("Past Question", days=-10)
        url = reverse("polls:results", args=(q.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, q.question_text)


class TestVoteView(TestCase):
    def test_vote_with_valid_choice(self):
        q = create_question_with_choice("Question", days=-1)
        choice = q.choice_set.first()
        url = reverse("polls:vote", args=(q.id,))
        response = self.client.post(url, {"choice": choice.id})

        self.assertEqual(response.status_code, 302)  # Redirect to results
        choice.refresh_from_db()
        self.assertEqual(choice.votes, 1)

    def test_vote_with_invalid_choice(self):
        q = create_question_with_choice("Question", days=-1)
        invalid_choice_id = 999
        url = reverse("polls:vote", args=(q.id,))
        response = self.client.post(url, {"choice": invalid_choice_id})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "choice does not exist")

    def test_vote_without_choice_key(self):
        q = create_question_with_choice("Question", days=-1)
        url = reverse("polls:vote", args=(q.id,))
        response = self.client.post(url, {})  # no "choice" key

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "choice does not exist")
