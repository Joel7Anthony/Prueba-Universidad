from django.db import models

# Create your models here.
class Task(models.Model):
    decano= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)