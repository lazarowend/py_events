from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Event


@receiver(pre_save, sender=Event)
def create_slug_event(sender, instance, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)
