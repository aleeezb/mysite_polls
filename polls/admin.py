from django.contrib import admin
from polls.models import Question , Choice

class Choiceinline(admin.StackedInline):
    model = Choice
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title and discription" , {"fields":["question_text"]}),
        ("dates" , {"fields": ["pub_date"]})
        
    ]
    inlines = [Choiceinline]
    list_display = ["pub_date","question_text","was_published"]
    list_filter = ["pub_date"]
    date_hierarchy = "pub_date"
    search_fields = ["question_text"]
    
# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)