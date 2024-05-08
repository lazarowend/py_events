from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Event
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import EventForm


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


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class ListUserEventView(ListView):
    model = Event
    template_name = 'my_events.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class CreateEventView(CreateView):
    model = Event
    template_name = 'new_event.html'
    form_class = EventForm
    success_url = reverse_lazy('list_user_event_view') 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
