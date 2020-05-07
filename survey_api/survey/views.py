from django.shortcuts import render

from rest_framework import viewsets
from .serializers import SurveySerializer
from .models import Survey

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
