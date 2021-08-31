from website.models import Event
from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Event


class DisplayEvent(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'date_created']


admin.site.register(Event, DisplayEvent)