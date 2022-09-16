from django.contrib import admin
from .models import (
                    Event
                    )

class EventAdmin(admin.ModelAdmin):#Customize the Django Admin Panel
    list_display = ['Title', 'Event_Time', 'Event_Day', 'treshold',
                    'created', 'updated']
admin.site.register(Event, EventAdmin)