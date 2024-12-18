from django.db import models
from django.contrib.auth.models import User
from adresses.models import Address


CHOICE_EVENT_TYPE = (
    ('Festa', 'Festa'),
    ('Reunião', 'Reunião')
)

CHOICE_TICKET_TYPE = (
    ('Inteira', 'Inteira'),
    ('Meia', 'Meia'),
)

CHOICE_IMAGE_TYPE = (
    ('Principal', 'Principal'),
    ('Extra', 'Extra'),
)


class Event(models.Model):
    name = models.CharField(max_length=150)
    type_event = models.CharField(choices=CHOICE_EVENT_TYPE, max_length=40)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    date_event = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='event_user')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='address')
    slug = models.SlugField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TicketType(models.Model):
    type_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.type_name}'


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='tickets')
    ticket_type = models.ForeignKey(TicketType, on_delete=models.PROTECT, related_name='ticket_type')
    price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=1)
    amount_sold = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.event}'


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='event_images')
    image = models.ImageField(upload_to='events/')
    type_image = models.CharField(choices=CHOICE_IMAGE_TYPE, max_length=50)

    def __str__(self):
        return f'{self.event}'
