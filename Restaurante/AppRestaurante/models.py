from django.db import models
from django.forms import DateField, DateTimeField

class Menu(models.Model):
    tipo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40) 

    def __str__(self):
        return f"{self.nombre}"
    
class Local(models.Model):
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40) 
    telefono = models.CharField(max_length=40)   
    exterior = models.CharField(max_length=5)
    capacidad_interior = models.IntegerField()  
    capacidad_exterior = models.IntegerField(blank=True, null=True)   

    def __str__(self):
        return f"{self.provincia} - {self.direccion}"
    
class Reserva(models.Model):
    nombre_completo = models.CharField(max_length=40)
    dia = models.CharField(max_length=10)
    horario = models.CharField(max_length=5)
    cantidad_personas = models.IntegerField() 
    lugar = models.CharField(max_length=15)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dia} - {self.horario}"

class Contacto(models.Model):
    motivo = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=50)
    telefono = models.IntegerField() 
    email = models.EmailField()
    mensaje = models.CharField(max_length=256)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_completo}"


