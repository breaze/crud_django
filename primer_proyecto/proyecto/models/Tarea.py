from django.db import models
from django.db.models.fields.related import ForeignKey

from proyecto.models.Persona import Persona

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    fecha_creacion = models.DateField()
    responsable = ForeignKey(Persona, on_delete=models.CASCADE)