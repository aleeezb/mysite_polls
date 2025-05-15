from polls.tests.halper import create_question
from django.test import TestCase
from django.urls import reverse





class Questionindexviewtest(TestCase):
    def test_no_question_shows_empty_page(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No questions available")
        self.assertQuerySetEqual(response.context["latest_question_list"],[])
        
    def test_index_page_shows_old_question(self):
        q = create_question(
            text= "sample",
            days=-10
        )
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response,q.question_text)
        self.assertEqual(response.status_code,200)  
        self.assertQuerySetEqual(response.context["latest_question_list"],[q]) 
        
    def test_future_question_not_shown(self):
        q = create_question(text="sample",days=10)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertQuerySetEqual(response.context["latest_question_list"],[])
        self.assertNotContains(response,q.question_text)
        
    def test_future_question_and_past_question_shows_only_past_question(self):
        q1_old = create_question(text="sample old",days=-10)
        q2_future = create_question(text="sample future",days=10)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertNotContains(response,q2_future.question_text)
        self.assertContains(response,q1_old.question_text)
        self.assertQuerySetEqual(response.context["latest_question_list"],[q1_old])
    
    def test_multiple_old_question_shows_all(self):
        q1 = create_question(text="sample 1",days=-10)
        q2 = create_question(text="sample 2",days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,q1.question_text)
        self.assertContains(response,q2.question_text)
        self.assertQuerySetEqual(response.context["latest_question_list"],[q2,q1])