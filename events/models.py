from django.db import models
from django.contrib.auth.models import User
from adresses.models import Address


CHOICE_TYPE = (
    (1, 'Festa'),
    (2, 'Reunião')
)


class Event(models.Model):
    name = models.CharField(max_length=150)
    type_event = models.IntegerField(choices=CHOICE_TYPE)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='events/') 
    created_at = models.DateTimeField(auto_now_add=True)
    date_event = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='address')
    max_tickets = models.IntegerField()
    slug = models.SlugField(null=True, blank=True)
    price_ticket = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    tickets_sold = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.name


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tickets')
    amount = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.event}'