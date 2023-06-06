from django.shortcuts import render , redirect
from . import forms

# Create your views here.
def index(request):
    return render (request, "inicio/index.html")

def Crear_Cliente(request):
    if request.method == "POST":
        form = forms.ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ( "inicio:index")
    else:
       form = forms.ClientesForm()
       context = {"form":form}
    return render (request, "inicio/Crear_Cliente.html", context)


def Crear_Mascota(request):
    if request.method == "POST":
        form = forms.MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ( "inicio:index")
    else:
       form = forms.MascotaForm()
       context = {"form":form}
    return render (request, "inicio/Crear_Mascota.html", context)
    
def Crear_Servicio(request):
    if request.method == "POST":
        form = forms.ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ( "inicio:index")
    else:
       form = forms.ServicioForm()
       context = {"form":form}
    return render (request, "inicio/Crear_Servicio.html", context)    