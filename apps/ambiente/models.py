from django.db import models

# Create your models here.
class Ambiente(models.Model):
    nombre = models.CharField(
        max_length=1000,
        blank=False,
        null=False
    )
    descripcion = models.TextField(
        max_length=5000,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Ambiente"
        verbose_name_plural = "Ambientes"

class Estante(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    descripcion = models.TextField(
        max_length=5000,
        blank=True,
        null=True
    )
    ambiente = models.ForeignKey(
        'ambiente.Ambiente',
        on_delete=models.CASCADE,
        related_name='estantes',
    )
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Estante"
        verbose_name_plural = "Estantes"

class Archivador(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    descripcion = models.TextField(
        max_length=5000,
        blank=True,
        null=True
    )
    estante = models.ForeignKey(
        'ambiente.Estante',
        on_delete=models.CASCADE,
        related_name='archivadores',
    )
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Archivador"
        verbose_name_plural = "Archivadores"

class Archivo(models.Model):
    nombre = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )
    descripcion = models.TextField(
        max_length=5000,
        blank=True,
        null=True
    )
    archivo = models.FileField(
        upload_to='archivos/',
        blank=False,
        null=False
    )
    archivador = models.ForeignKey(
        'ambiente.Archivador', 
        on_delete=models.CASCADE,
        related_name='archivos'
    )
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
    