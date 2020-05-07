from django.db import models

class Survey(models.Model):
    question = models.CharField(max_length=255)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.question
