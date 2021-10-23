from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    is_removed = models.BooleanField(default=False)
    title = models.CharField(max_length=150)
    content = models.TextField()
    register = models.CharField(max_length=200)
    flyer = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(auto_now=False)
    slug = models.SlugField(blank=True)
    event_is_live = models.BooleanField()
    is_hustle_chat = models.BooleanField(default=False)
    yt_link = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
