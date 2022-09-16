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

urlpatterns = [
    path('', include(router.urls), name = 'Reminder'),
    path('api-auth', include('rest_framework.urls', namespace = 'rest_framework'))
]
