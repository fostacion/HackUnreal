# problems/views.py
from rest_framework import generics
from .models import Problem
from .serializers import ProblemSerializer

class ProblemListView(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer