from django.db import models
from django.utils import timezone
import datetime as dt 
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return f"{self.question_text} ({self.id})"
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description=" pulished recently?"
        
        
    )
    
    def was_published(self):
        return self.pub_date > timezone.now() - dt.timedelta(days=1) and self.pub_date < timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.choice_text} ({self.question.id})"