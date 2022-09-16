from django.contrib import admin
from django.contrib.auth.models import(
    User,
)
from .models import (
                    Event,
                    )

class EventAdmin(admin.ModelAdmin):#Customize the Django Admin Panel
    list_display = ['Title', 'Upcoming_DateTime', 'treshold',
                    'Repeat_all_Day','Repeat','created', 'updated']
admin.site.register(Event, EventAdmin)


#class UserAdmin(admin.ModelAdmin):
#    list_display = ["email", "is_staff", "is_active"]
#admin.site.register(MyUser, UserAdmin)