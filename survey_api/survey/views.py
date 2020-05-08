from django.shortcuts import render

from rest_framework import viewsets
from .serializers import SurveySerializer, UserSerializer, SurveyUserSerializer
from .models import Survey, Users, Survey_Users

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class SurveyUserViewSet(viewsets.ModelViewSet):
    queryset = Survey_Users.objects.all()
    serializer_class = SurveyUserSerializer