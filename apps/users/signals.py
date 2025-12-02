from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Crea un perfil para un nuevo usuario o se asegura de que uno exista
    para un usuario existente que se está guardando.
    """
    if created:
        Profile.objects.create(user=instance)
    else:
        # Para usuarios existentes, nos aseguramos de que tengan un perfil.
        # Esto soluciona el problema para usuarios creados antes de implementar los perfiles.
        Profile.objects.get_or_create(user=instance)