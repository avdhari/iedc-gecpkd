from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    register = models.CharField(max_length=200)
    # flyer = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=timezone.now)
    event_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title
