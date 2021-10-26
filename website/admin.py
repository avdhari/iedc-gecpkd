from django.contrib import admin
from website.models import Event, HustleChat


class DisplayEvent(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'date_created']


admin.site.register(Event, DisplayEvent)
admin.site.register(HustleChat)