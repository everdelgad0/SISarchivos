from django.db import models

# Create your models here.
class Permisos(models.Model):
    class Meta:
        permissions = [
            ("users", "modulo de usuarios"),
            ("ambiente", "modulo de sistema de archivos"),
            ("archivo", "modulo de vista de archivos"),
        ]
        managed = False