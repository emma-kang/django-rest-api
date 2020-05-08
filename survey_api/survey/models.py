from django.db import models

class Survey(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Results(models.Model):
    username = models.CharField(max_length=50)
    useremail = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)

    def __str__(self):
        return self.username