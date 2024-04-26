from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event


class ListEventView(ListView):
    model = Event
    template_name = 'home.html'
    


class DetailEventView(DetailView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'event'