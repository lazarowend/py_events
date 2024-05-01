from django.views.generic import ListView, DetailView
from .models import Event


class ListEventView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'events'
    
    queryset = Event.objects.order_by('status', 'date_event')


class DetailEventView(DetailView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'event'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
