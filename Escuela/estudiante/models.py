from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Estudiante(models.Model):
    usuario = models.OneToOneField("clase.Estudiante", on_delete=models.CASCADE, related_name="estudiante")
    celular = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self) -> str:
        return self.usuario.nombre

class Clase(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True, blank=True)
    comision = models.ForeignKey("clase.Comision", on_delete=models.DO_NOTHING)
    fecha_inscripcion = models.DateTimeField(editable=False, default=timezone.now)

    class Meta: 
        ordering = ("-fecha_inscripcion",)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)