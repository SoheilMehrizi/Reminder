from django.db import models
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    Title = models.CharField("Title", max_length=100, blank=True)
    description = models.TextField("Description")
    logo = models.URLField("Logo", max_length=200)
    treshold = models.PositiveIntegerField("Treshold")
    Event_Time = models.TimeField("Event_Time", auto_now=False, auto_now_add=False)
    Event_Day = models.DateField("Event_Date", auto_now=False, auto_now_add=False)
    created = models.DateTimeField("Created_Date", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)
