from datetime import datetime, timedelta
from faulthandler import disable
from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import (
                    viewsets,
                    permissions
                            )
from rest_framework.views import APIView
from .models import(
        Event,

)
from .serializers import(
        Event_Serializer,
                        )




class EventViewSet(viewsets.ModelViewSet):
         """
         API endpoint for Show, create, edit or delete the Event Object
         """
         queryset = Event.objects.all()
         serializer_class = Event_Serializer
         permision_classes = [permissions.IsAuthenticated]
         def _get_upcomings(self):
                """
                filter the upcoming Events and email them
                Hint: the date Time format is : %d-%m-%Y %H:%M:%S
                """
                Events = Event.objects.filter(disabled = False).order_by("Upcoming_DateTime")
                for item in list(Events):
                        Upcoming_Time = item.Upcoming_DateTime.strftime("%H:%M")
                        minute = int(item.Upcoming_DateTime.strftime("%M")) - abs(item.treshold)#-1
                        hour = int(item.Upcoming_DateTime.strftime("%H"))
                        while(minute < 0):
                                if hour == 0:
                                        hour = 23
                                        minute = 60 - abs(minute)
                                else:
                                        hour -= 1
                                        minute = 60 - abs(minute)
                        Upcoming_Time = f"{hour}:{minute}"
                        print(Upcoming_Time)
                        Upcoming_date = item.Upcoming_DateTime.date()
                        Current_Date = datetime.now().date()
                        dateandTime = datetime.now()
                        Current_Time_H = int(dateandTime.strftime("%H"))
                        Current_Time_M = int(dateandTime.strftime("%M"))
                        Current_Time = f"{Current_Time_H}:{Current_Time_M}"
                        print(f"curenttiem:{Current_Time}")
                        print(f"upcomingtime:{Upcoming_Time}")
                        Time_Status = (Current_Time == Upcoming_Time)
                        if (Current_Date == Upcoming_date):
                                if (Time_Status):
                                        try:
                                            #Trying to Notify the Person in Email_Update The Object and Shift the date
                                            if (item.Repeat_all_Day):
                                                """
                                                If event is a all day event every time that event passed , shift the date for a day
                                                """
                                                updated_date = item.Upcoming_DateTime + timedelta(days=1)
                                                EventObj = Event.objects.filter(id = int(item.id)).update(Upcoming_DateTime = updated_date)
                                                EventObj.save()

                                            elif (item.Repeat != 0):
                                                """
                                                for Repeat times Repeat the Event
                                                """
                                                updated_date = item.Upcoming_DateTime + timedelta(days=1)
                                                repeat = item.Repeat - 1
                                                if repeat == 0:
                                                        EventObj = Event.objects.filter(id = int(item.id)).update(Upcoming_DateTime = updated_date,
                                                                                                                  Repeat = repeat, disabled = True)
                                                        EventObj.save()                                                        
                                                else:
                                                        EventObj = Event.objects.filter(id = int(item.id)).update(Upcoming_DateTime = updated_date,
                                                                                                                  Repeat = repeat)
                                                        EventObj.save()

                                            else:
                                                """
                                                if Event not repeatable true disbled status to the True
                                                """
                                                EventObj = Event.objects.filter(id = int(item.id)).update(disabled = True)
                                                EventObj.save()
                                            print(f"Upcoming Event: {item.Title}\n{item.description}\n{item.logo}")

                                        except :
                                            print("fucked UP!")
                        print(f"itemID:{item.id}\nUpcoming_min: {Upcoming_Time}is_now?{Current_Time == Upcoming_Time}, Upcoming_date: {Upcoming_date}/is_now?{Current_Date == Upcoming_date}")
#class UserViewSet(viewsets.ModelViewSet):
#        """
#        User Api endpoint for Show, create, edit or delete the 
#        User Object
#        """

#        queryset = MyUser.objects.all()
#        serializer_class = User_Serializer
#        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SomeView(APIView):
     def get(self, request):
        """
        return upcomming requests
        """
        dateandTime = datetime.now()
        Current_Time = dateandTime.strftime("%H:%M")
        Current_Date = datetime.now().date()
        upcomings = list(Event.objects.all())
        print(f"{Current_Time}\n,{Current_Date}, {upcomings}")
        return Response(len(upcomings))