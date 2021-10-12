from django.shortcuts import render, HttpResponse
from servicios.models import Servicio


# Create your views here.

def inicio(request):
    return render(request, "TOApp/inicio.html")


# def servicios(request):
#     servicios=Servicio.objects.all()
#     return render(request, "TOApp/servicios.html", {"servicios": servicios})


# def tienda(request):
#     return render(request, "TOApp/tienda.html")


def nosotros(request):
    return render(request, "TOApp/nosotros.html")


def contacto(request):
    return render(request, "TOApp/contacto.html")
