from django.db import models


# Create your models here.

class Dairy(models.Model):
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
