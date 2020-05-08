# convert model instance to other format

from rest_framework import serializers
from .models import Survey, Results

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'question')

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ('id', 'username', 'useremail', 'answer1', 'answer2', 'answer3', 'answer4')