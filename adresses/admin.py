from django.contrib import admin
from .models import Address


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('zip_code', 'state', 'city', 'district', 'road', 'get_user')
    search_fields = ('zip_code',)

    def get_user(self, obj):
        return obj.user.username
