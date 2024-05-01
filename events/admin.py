from django.contrib import admin
from .models import Event, Ticket

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'description', 'created_at', 'date_event', 'user', 'address','max_tickets', 'price_ticket', 'tickets_sold','slug')
    

@admin.register(Ticket)
class AdminTicket(admin.ModelAdmin):
    list_display = ('event', 'user')
    search_fields = ('event', 'user')