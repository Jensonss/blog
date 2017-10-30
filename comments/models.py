from django.db import models

# Create your models here.
from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('myblog.Post')

    def __str__(self):
        return self.text[:20]
