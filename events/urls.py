from django.urls import path
from .views import ListEvents


urlpatterns = [
    path('events/', ListEvents.as_view(), name='list_events')
]
