from django.db import models
from django.forms import CharField, DateField, IntegerField

class Menu(models.Model):
    tipo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40) 
    #desayuno_merienda = models.CharField(max_length=40)
    
class Local(models.Model):
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40) 
    telefono = models.CharField(max_length=40)   
    exterior = models.CharField(max_length=5)
    capacidad_interior = models.IntegerField()  
    capacidad_exterior = models.IntegerField()   
    
class Reserva(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    cantidad_personas = models.IntegerField() 
    lugar = models.CharField(max_length=15)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)


class Contacto(models.Model):
    motivo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) 
    telefono = models.IntegerField() 
    email = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=256)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)


