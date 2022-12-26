from django.db import models

# Create your models here.

class familia (models.Model):
    nombre = models.CharField (max_length=100)
    edad = models.IntegerField()
    esta_casado = models.BooleanField()