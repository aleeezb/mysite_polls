from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question

class Questionmodeltest(TestCase):
    def test_was_published_future_question(self):
        future_question = Question(
            question_text = "sample question",
            pub_date = timezone.now() + datetime.timedelta(days=2)
            
        )
        self.assertIs(future_question.was_published(),False,"wrong value for was_pulished_recently ")
    
    def test_was_published_5_min(self):
        question = Question(
            question_text= "sample",
            pub_date = timezone.now() - datetime.timedelta(minutes=5)
            
        )
        self.assertIs(question.was_published(),True,"wrong value for was_pulished_recently ")
    
    def test_was_published_10_days_ago(self):
        question = Question(
            question_text = "sample",
            pub_date = timezone.now() - datetime.timedelta(days=10)
            
        )
        self.assertIs(question.was_published(),False,"wrong value for was_pulished_recently ")