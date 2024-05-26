from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre
    
class Comision(models.Model):
    nombre = models.PositiveIntegerField(unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
    estudiante = models.ManyToManyField(Estudiante)

    def __str__(self) -> str:
        return f"Curso de {self.curso.nombre}" if self.curso else f"Comision {self.nombre}"