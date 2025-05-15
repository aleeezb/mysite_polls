from polls.models import Question
import datetime
from django.utils import timezone



def create_question(text, days):
    return Question.objects.create(
        question_text=text,
        pub_date=timezone.now() + datetime.timedelta(days=days)
    )