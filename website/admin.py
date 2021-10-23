from django.contrib import admin
from website.models import Event


class DisplayEvent(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'date_created']


admin.site.register(Event, DisplayEvent)
