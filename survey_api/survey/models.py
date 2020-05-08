from django.db import models

class Survey(models.Model):
    question = models.CharField(max_length=255)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.question

class Users(models.Model):
    useremail = models.CharField(max_length=255)
    passwords = models.CharField(max_length=255)

    def __str__(self):
        return self.useremail

class Survey_Users(models.Model):
    userid = models.CharField
    surveyid = models.CharField
    answers = models.CharField(max_length=255)

    def __str__(self):
        return self.userid
