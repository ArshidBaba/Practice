from rest_framework import generics
from rest_framework import filters

from .models import Question
from .serializers import QuestionSerializer

class QuestionAPIView(generics.ListCreateAPIView):
    # search_fields = ['question_text']
    # filter_backends = (filters.SearchFilter)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


