from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path("Crear_Cliente/", views.Crear_Cliente, name="Crear_Cliente"),
    path("Crear_Mascota/", views.Crear_Mascota,name="Crear_Mascota"),
    path("Crear_Servicio/", views.Crear_Servicio, name="Crear_Servicio"),
]
