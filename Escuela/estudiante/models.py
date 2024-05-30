from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

# Create your models here.

class Admin(AbstractUser):
        groups = models.ManyToManyField(
        Group,
        related_name='admin_set',  # Cambio aquí
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

        user_permissions = models.ManyToManyField(
        Permission,
        related_name='admin_user_set',  # Cambio aquí
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

        def __str__(self) -> str:
            return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username

class Estudiante(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="estudiante")
    celular = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.usuario.username}"

class Clase(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True, blank=True)
    comision = models.ForeignKey("clase.Comision", on_delete=models.DO_NOTHING)
    fecha_inscripcion = models.DateTimeField(editable=False, default=timezone.now)

    class Meta: 
        ordering = ("-fecha_inscripcion",)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)