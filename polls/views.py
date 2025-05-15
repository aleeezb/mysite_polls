from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question , Choice
from django.utils import timezone
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from django.views import generic



# def index_view(request):
#     questions =Question.objects.order_by("pub_date").all()[:10]
#     context = {"latest_question_list":questions}
#     return render(request,"polls/index.html",context)

class Indexview(generic.ListView):
    template_name="polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        now = timezone.now()
        return Question.objects.filter(pub_date__lte=now).order_by("-pub_date")[:10]

class Detailview(generic.DeleteView):
    template_name = "polls/detail.html"
    model = Question
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    def not_return_the_future_qurstion(request, question_id):
        question = get_object_or_404(Question , pk=question_id)
        if question.pub_date > timezone.now():
            raise Http404("quesstion not published yet")
        return render(request, "polls/detail.html", {"question": question})


class Resultview(generic.DeleteView):
    template_name = "polls/results.html"
    model = Question

def vote (request,question_id):
    question= get_object_or_404(Question,id=question_id)
    
    try:
        choice_id = request.POST["choice"]
        choice = question.choice_set.get(id=choice_id)
    except (Choice.DoesNotExist,KeyError):
        context = {
            "question":question,
            "error" : f"choice does not exist ):"
            
        }
        return render(request,"polls/detail.html",context)
    choice.votes +=1
    choice.save()
    
    return HttpResponseRedirect(reverse("polls:results",args=(question_id, )))


































 #creating a new object
    # q = Question(question_text ="best persian food",pub_date =timezone.now())
    # q.save()
    # Questions = Question.objects.all()
    # q = Questions[0]
    # print(q.pub_date,q.was_published())
    
    
    # Questions = Question.objects.filter(id__gt =8)
    # print(Questions)
    # Questions = Question.objects.filter(question_text__startswith ="what")
    # print(Questions)
    # Questions = Question.objects.filter(pub_date__year =2025)
    # print(Questions)
    
    # c  = Choice(question= q,choice_text = "asqar")
    # c.save()
    # c  = Choice(question= q,choice_text = "akbar")
    # c.save()
    # c  = Choice(question= q,choice_text = "ahmad")
    # c.save()
    
    # q = Question.objects.get(id=11)
    # choice = Choice.objects.filter(question =q)
    # print(choice)
    # choice = q.choice_set.all()