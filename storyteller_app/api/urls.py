from rest_framework import routers
from .views import EventsViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'storyteller_app', EventsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
