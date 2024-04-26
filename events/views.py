from django.shortcuts import render
from django.views.generic import ListView
from .models import Event


class ListEvents(ListView):
    model = Event
    template_name = 'home.html'
    