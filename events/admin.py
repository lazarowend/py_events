from django.contrib import admin
from .models import Event

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'description', 'created_at', 'date_event', 'user', 'address','max_tickets', 'slug')