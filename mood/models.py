from django.db import models


# Create your models here.
class Mood(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
