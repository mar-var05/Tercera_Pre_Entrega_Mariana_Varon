from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Clientes)
admin.site.register(models.Mascota)
admin.site.register(models.Servicio)