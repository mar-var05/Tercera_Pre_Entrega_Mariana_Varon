from django import forms

from . import models

class ClientesForm(forms.ModelForm):
    class Meta:
        model = models.Clientes
        fields = "__all__"


class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = "__all__"


class ServicioForm(forms.ModelForm):
    class Meta:
        model = models.Servicio
        fields = "__all__"



