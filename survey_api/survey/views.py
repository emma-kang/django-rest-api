from django.shortcuts import render

from rest_framework import viewsets
from .serializers import SurveySerializer, ResultsSerializer
from .models import Survey, Results

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer