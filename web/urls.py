from django.urls import(
                        include,
                        path,
                        )
from rest_framework import(
                        routers,
                        )
from . import(
              views,
              )

router = routers.DefaultRouter()
router.register(r"Events",views.EventViewSet, basename="Event")
#router.register(r'someView', views.SomeView, basename="SomeView")

#router.register(r"ListUsers",views.ListUsers.as_view(), basename="ListUsers")
urlpatterns = [
    path('', include(router.urls), name = 'Reminder'),
    path('Reminder/', views.ReminderAPI.as_view(),name="SomeView"),
    path('api-auth', include('rest_framework.urls', namespace = 'rest_framework')),
    #path('someView', views.SomeView, name="Some_View")
]
