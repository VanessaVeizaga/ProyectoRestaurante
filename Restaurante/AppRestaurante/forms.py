from datetime import datetime
from logging import PlaceHolder
from django import forms

from .models import Local

class MenuFormulario(forms.Form):
    opciones = (("Entrada","Entrada"), ("Plato principal","Plato Principal"), ("Postre","Postre"), ("Desayuno-Merienda","Desayuno-Merienda"))
    tipo = forms.ChoiceField(choices= opciones)
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(label="Descripción", max_length=128) 

class LocalFormulario(forms.Form):
    provincia = forms.CharField(max_length=40)
    localidad = forms.CharField(max_length=40)
    direccion = forms.CharField(label="Dirección", max_length=40) 
    telefono = forms.CharField(label="Teléfono", max_length=40)   
    exterior = forms.ChoiceField(label="¿Posee patio o terraza?", choices= (("Sí", "Sí"), ("No", "No")))
    capacidad_interior = forms.IntegerField(label="Capacidad interior")  
    capacidad_exterior = forms.IntegerField(label="Capacidad exterior", required=False) 

class ReservaFormulario(forms.Form):
    horarios = opciones = (("10:00","10:00"), ("12:00","12:00"), ("14:00","14:00"), ("16:00","16:00"), ("18:00","18:00"), ("20:00","20:00"), ("22:00","22:00"))
    nombre_completo = forms.CharField(label="Nombre completo")
    dia = forms.DateField(label="Día")
    horario = forms.ChoiceField(choices=horarios)
    cantidad_personas = forms.IntegerField(label="Cantidad de personas") 
    lugar = forms.ChoiceField(choices=(("Dentro","Dentro"), ("Fuera","Fuera")))
    local = forms.ModelChoiceField(queryset=Local.objects.all())

class ContactoFormulario(forms.Form):
    motivo = forms.ChoiceField(choices=(("Consulta","Consulta"), ("Sugerencia","Sugerencia"), ("Reclamo","Reclamo")))
    nombre_completo = forms.CharField(max_length=50)
    telefono = forms.IntegerField(label="Teléfono") 
    email = forms.CharField(max_length=30)
    mensaje = forms.CharField(max_length=256)
    local = forms.ModelChoiceField(queryset=Local.objects.all(), required=False)