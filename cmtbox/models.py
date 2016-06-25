from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Member(models.Model):
    name=models.CharField(max_length=50)
    relation=models.CharField(max_length=50)
    thought=models.TextField()
    post_date=models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.relation

# Create your models here.
