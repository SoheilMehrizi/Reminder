
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
                  "Repeat","Repeat_all_Day","disabled","Upcoming_DateTime", "created", "updated"]


#class User_Serializer(serializers.HyperlinkedModelSerializer):

#    class Meta:
#        model = MyUser
#        field = ["email", "password"]
