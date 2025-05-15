from django.urls import path
from polls import views
from polls.views import Indexview,Detailview,Resultview

app_name = 'polls' 

urlpatterns = [
    path("", Indexview.as_view(), name="index"),
    path("<int:pk>", Detailview.as_view(), name="detail"),
    path("<int:pk>/result", Resultview.as_view(), name="results"),
    path("<int:question_id>/vote", views.vote, name="vote"),
]
