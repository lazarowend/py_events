from django.contrib import admin
from .models import Address


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('place_name', 'state', 'city', 'district', 'road', 'user')
    search_fields = ('place_name',)
