from django.contrib import admin
from website.models import *


class DisplayEvent(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'date_created']


class DisplayTeam(admin.ModelAdmin):
    list_display = ['name', 'position']


admin.site.register(Event, DisplayEvent)
admin.site.register(HustleChat)
admin.site.register(NodalOfficer)
admin.site.register(TeamMember, DisplayTeam)
