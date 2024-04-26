from django.urls import path
from .views import ListEventView, DetailEventView


urlpatterns = [
    path('events/', ListEventView.as_view(), name='list_event_view'),
    path('event/', DetailEventView.as_view(), name='detail_event_view')
]
