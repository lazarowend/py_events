from django.urls import path
from .views import CreateAddressView, ListAddressView, UpdateAddressView, DeleteAddressView


urlpatterns = [
    path('events/adresses', ListAddressView.as_view(), name='list_address_view'),
    path('events/create_address', CreateAddressView.as_view(), name='create_address_view'),
    path('events/update_address/<int:pk>', UpdateAddressView.as_view(), name='update_address_view'),
    path('events/delete_address/<int:pk>', DeleteAddressView.as_view(), name='delete_address_view')
]
