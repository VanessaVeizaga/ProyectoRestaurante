from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return HttpResponse("Vista Inicio")

def menu(request):
    return HttpResponse("Vista Menú")

def local(request):
    return HttpResponse("Vista Local")

def reserva(request):
    return HttpResponse("Vista Reserva") 

def contacto(request):
    return HttpResponse("Vista Contacto")        


