from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    numero_movil = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=15)
    especie = models.CharField(max_length=10)
    raza = models.CharField(max_length=15)
    edad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_mascota


class Servicio(models.Model):
    tipo_de_servicio = models.CharField(max_length=20)
    servicio_completado = models.BooleanField()

    def __str__(self):
        return self.tipo_de_servicio

