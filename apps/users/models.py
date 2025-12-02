from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Modelo que extiende el modelo User de Django para añadir campos adicionales.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(
        upload_to='users/pictures/', 
        default='users/pictures/default.png', 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Create your models here.
class Permisos(models.Model):
    class Meta:
        permissions = [
            ("users", "modulo de usuarios"),
            ("ambiente", "modulo de sistema de archivos"),
            ("archivo", "modulo de vista de archivos"),
        ]
        managed = False