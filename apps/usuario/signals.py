from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, ProfileUser
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=CustomUser)
def create_or_update_profileuser(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)
        logger.info(f'Se ha creado el perfil para el usuario {instance.username}')
    else:
        instance.profile.save()
        logger.info(f'Perfil del usuario {instance.username} actualizado')