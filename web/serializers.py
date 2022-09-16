from rest_framework import(
    serializers
)
from .models import(
    Event,
)


class Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["Title", "description", "logo", "treshold",
                  "Event_Time", "Event_Day", "created", "updated"]