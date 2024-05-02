from .models import Event, Ticket
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from adresses.models import Address


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


@login_required
def get_infos_events_tickets_address_user(request):
    user = request.user

    amount_user_tickets_purchased = Ticket.objects.filter(user=user).count()

    amount_user_tickets_sold = Event.objects.filter(user=user).aggregate(total_sold_tickets=Sum('tickets_sold'))['total_sold_tickets']

    amount_user_created_events = Event.objects.filter(user=user).count()

    amount_user_address = Address.objects.filter(user=user).count()
    
    serialized_amount = {
        'amount_user_tickets_purchased': amount_user_tickets_purchased,
        'amount_user_tickets_sold': amount_user_tickets_sold,
        'amount_user_created_events': amount_user_created_events,
        'amount_user_address': amount_user_address
    }

    return JsonResponse(serialized_amount)
