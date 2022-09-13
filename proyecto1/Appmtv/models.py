from django.db import models

class Familia(models.Model):
    nombre_apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nac = models.DateField()