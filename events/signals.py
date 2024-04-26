import uuid
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Event


def generate_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    uuid_filename = f"{uuid.uuid4().hex}.{ext}"
    
    return os.path.join('events', uuid_filename)


@receiver(pre_save, sender=Event)
def rename_event_image(sender, instance, **kwargs):
    current_filename = instance.image.name
    new_filename = generate_image_filename(instance, current_filename)
    instance.image.name = new_filename


@receiver(pre_save, sender=Event)
def set_slug_event(sender, instance, **kwargs):
    print('aqui')
    instance.slug = uuid.uuid4().hex
