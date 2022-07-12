

from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from session.models import Session


@receiver(post_save, sender=User)
def create(sender, instance, created, **kwargs):
    if created:
         Session.objects.update(user_id=instance.id)
