from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    imagen = models.ImageField(upload_to='avatar', null=True, blank=True)

class Menu(models.Model):
    tipo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=128) 
    imagen = models.ImageField(upload_to='menu', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
class Local(models.Model):
    provincia = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40) 
    telefono = models.CharField(max_length=15)   
    capacidad = models.IntegerField()  
    imagen = models.ImageField(upload_to='local', null=True, blank=True)

    def __str__(self):
        return f"{self.provincia} - {self.localidad} - {self.direccion}"
    
class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.CharField(max_length=5)
    cantidad_personas = models.PositiveIntegerField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.local} - {self.dia} - {self.horario}"

class Contacto(models.Model):
    motivo = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15) 
    email = models.EmailField()
    mensaje = models.CharField(max_length=256)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_completo}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default="2022-05-02 19:22:11.517108")
    contenido = models.CharField(max_length=256)
    imagen = models.ImageField(upload_to='posts', null=True, blank=True)

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default="2022-05-02 19:22:11.517108")
    contenido = models.CharField(max_length=256)  


    


    

    
    
   


    




