import uuid
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Event, Ticket


def generate_image_filename(instance, filename):
    if not instance.pk:
        ext = os.path.splitext(filename)[-1]
        uuid_filename = f"{uuid.uuid4().hex}{ext}"
        return os.path.join('events', uuid_filename)
    return filename

@receiver(pre_save, sender=Event)
def rename_event_image(sender, instance, **kwargs):
    instance.image.name = generate_image_filename(instance, instance.image.name)


@receiver(pre_save, sender=Event)
def set_slug_event(sender, instance, **kwargs):
    print('aqui')
    instance.slug = uuid.uuid4().hex


@receiver(pre_save, sender=Ticket)
def set_tickets_sold(sender, instance, **kwargs):
    event = instance.event
    if event.tickets_sold >= event.max_ticket:
        event.status = False
        event.save()
    else:
        event.tickets_sold += instance.amount
        event.save()
