from django.urls import path, include

from . import views

urlpatterns = [
    path('questions/', views.QuestionAPIView.as_view())
]