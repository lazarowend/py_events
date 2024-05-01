from .models import Event
from django.http import JsonResponse
from django.contrib.auth.models import User


def search_events(request, name):
    events = Event.objects.filter(name__icontains=name)
    if name == 'all':
        events = Event.objects.all()

    serialized_events = [
        {
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'image': event.image.url,
            'created_at': event.created_at,
            'date_event': event.date_event,
            'user': event.user.username,
            'max_tickets': event.max_tickets,
            'slug': event.slug,
            'price_ticket': event.price_ticket,
            'status': event.status,
            'tickets_sold': event.tickets_sold,
        }
        for event in events
    ]
    
    return JsonResponse(serialized_events, safe=False)


def get_username(request, id):
    user = User.objects.get(id=id)
    
    if user is None:
        return JsonResponse({'status': 404})
    
    username = user.username    
    return JsonResponse(username, safe=False)