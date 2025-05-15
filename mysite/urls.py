
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path("polls/",include("polls.urls")),
    path("__debug__/", include("debug_toolbar.urls"))
]
