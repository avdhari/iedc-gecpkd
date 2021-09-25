from typing import Sized
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    register = models.CharField(max_length=200)
    flyer = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(auto_now=False)
    slug = models.SlugField(blank=False)
    event_is_live = models.BooleanField()
    is_hustle_chat = models.BooleanField(default=False)
    yt_link = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
