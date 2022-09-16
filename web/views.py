from django.shortcuts import render
from django.shortcuts import render
from rest_framework import (
                    viewsets,
                    permissions
                            )
from .models import(
        Event
)
from .serializers import(
        Event_Serializer
                        )




class EventViewSet(viewsets.ModelViewSet):
         """
         API endpoint for Show, create, edit or delete the Event Object
         """
         queryset = Event.objects.all().order_by("created")
         serializer_class = Event_Serializer
         permision_classes = [permissions.IsAuthenticated]
