from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

#Acceso a los sitios
def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

#Acceso a los vehiculos
def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "autos/index.html", {'vehiculos': vehiculos})

def crear(request):
    formulario = VehiculoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vehiculos')
    return render(request, "autos/crear.html", {'formulario': formulario})

def editar(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    formulario = VehiculoForm(request.POST or None, request.FILES or None, instance=vehiculo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('vehiculos')
    return render(request, "autos/editar.html", {'formulario': formulario})

def eliminar(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    return redirect('vehiculos')