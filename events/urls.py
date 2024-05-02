from django.urls import path
from .views import ListEventView, DetailEventView
from .ajax_views import search_events, get_infos_events_tickets_address_user


urlpatterns = [
    path('events/', ListEventView.as_view(), name='list_event_view'),
    path('events/detail/<slug:slug>/', DetailEventView.as_view(), name='detail_event_view')
]


ajax_urlpatterns = [
    path('events/search_events/<str:name>', search_events, name='search_events'),
    path('events/get_infos_events_tickets_address_user', get_infos_events_tickets_address_user, name='get_infos_events_tickets_address_user'),
]


urlpatterns += ajax_urlpatterns