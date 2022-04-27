from django.db import models
from django.forms import DateField, DateTimeField

class Menu(models.Model):
    tipo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=128) 
    imagen = models.ImageField()

    def __str__(self):
        return f"{self.nombre}"
    
class Local(models.Model):
    provincia = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40) 
    telefono = models.CharField(max_length=15)   
    capacidad = models.IntegerField()  

    def __str__(self):
        return f"{self.provincia} - {self.direccion}"
    
class Reserva(models.Model):
    nombre_completo = models.CharField(max_length=40)
    dia = models.DateField()
    horario = models.CharField(max_length=5)
    cantidad_personas = models.PositiveIntegerField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

  #  def __str__(self):
   #     return f"{self.local} {self.dia} {self.horario} {self.cantidad_personas}"

class Contacto(models.Model):
    motivo = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15) 
    email = models.EmailField()
    mensaje = models.CharField(max_length=256)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_completo}"

class reservasManager(models.Manager):
    def filtrar_reservas(self, local, dia, horario):
        reservas = self.filter(local__icontains = local, dia__icontains = dia, horario__icontains = horario)
        return reservas



