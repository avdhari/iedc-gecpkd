from django.db import models
from django.db.models.aggregates import Max
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
from website.tasks import image_url_split

class BaseModel(models.Model):
    class Meta:
        abstract = True
        app_label = 'website'


class Event(BaseModel):
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


class HustleChat(BaseModel):
    name_of_guest = models.CharField(blank=True, max_length=250)
    episode = models.IntegerField()
    video = EmbedVideoField()

    def __str__(self):
        return "Episode " + str(self.episode) + ": " + self.name_of_guest



class NodalOfficer(BaseModel):
    name = models.CharField(max_length=200)
    profile_image = models.URLField()
    linkedin_url = models.CharField(blank=True, max_length=250)
    twitter_url = models.CharField(blank=True, max_length=250)
    instagram_url = models.CharField(blank=True, max_length=250)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.profile_image = image_url_split(self.profile_image)
        super(NodalOfficer, self).save(*args, **kwargs)


class TeamMember(BaseModel):
    name = models.CharField(max_length=200)
    profile_image = models.URLField()
    linkedin_url = models.CharField(blank=True, max_length=250)
    twitter_url = models.CharField(blank=True, max_length=250)
    instagram_url = models.CharField(blank=True, max_length=250)
    POSITION = [
        ('Student Lead', 'Student Lead'),
        ('Technology Lead', 'Technology Lead'),
        ('Quality and Operations Lead', 'Quality and Operations Lead'),
        ('Community Lead', ' Community Lead'),
        ('Creative and Innovations Lead', 'Creative and Innovations Lead'),
        ('Finance Lead', 'Finance Lead'),
        ('Branding and Marketing Lead', 'Branding and Marketing Lead'),
    ]
    position = models.CharField(max_length=50, choices=POSITION)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.profile_image = image_url_split(self.profile_image)
        super(TeamMember, self).save(*args, **kwargs)
