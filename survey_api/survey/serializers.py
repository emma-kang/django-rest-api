# convert model instance to other format

from rest_framework import serializers
from .models import Survey, Users, Survey_Users

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'question', 'category')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'useremail', 'passwords')

class SurveyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey_Users
        fields = ('id', 'userid', 'surveyid', 'answer')