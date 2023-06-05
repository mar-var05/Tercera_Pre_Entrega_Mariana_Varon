from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    numero_movil = models.CharField(max_length=15)


class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=15)
    especie = models.CharField(max_length=10)
    raza = models.FloatField(max_length=15)
    edad = models.CharField(max_length=10)


class Servicio(models.Model):
    tipo_de_servicio = models.CharField(max_length=10)
    descripcion_del_servicio = models.CharField(max_length=30)
    servicio_completado = models.BooleanField()
    
