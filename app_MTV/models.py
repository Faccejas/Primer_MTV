from django.db import models

# Create your models here.

class Familia (models.Model):
    Nombre_Apellido = models.CharField(max_length = 50)
    Celular = models.IntegerField()
    Fecha_Nacimiento = models.DateField()
