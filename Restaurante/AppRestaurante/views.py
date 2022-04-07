from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")
    

def menu(request):
    return render(request, "menu.html")


def local(request):
    return render(request, "local.html")


def reserva(request):
    return render(request, "reserva.html")

def contacto(request):
    return render(request, "contacto.html")
    


