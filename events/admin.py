from django.contrib import admin
from .models import Event, Ticket, TicketType, EventImage


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'description', 'created_at', 'date_event', 'user', 'address', 'slug')


@admin.register(Ticket)
class AdminTicket(admin.ModelAdmin):
    list_display = ('event',)
    search_fields = ('event',)


@admin.register(TicketType)
class AdminTicketType(admin.ModelAdmin):
    list_display = ('type_name',)
    search_fields = ('type_name',)


@admin.register(EventImage)
class AdminEventImage(admin.ModelAdmin):
    list_display = ('event',)
    search_fields = ('event',)
