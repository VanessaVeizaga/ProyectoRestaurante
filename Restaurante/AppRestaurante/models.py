from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    imagen = models.ImageField(upload_to='avatar', default='avatar/perfil.png', null=True, blank=True)

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
        return f"{self.provincia} - {self.direccion}"
    
class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservas")
    dia = models.DateField()
    horario = models.CharField(max_length=5)
    cantidad_personas = models.PositiveIntegerField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return f"Local: {self.local} - Fecha: {self.dia} - Hora: {self.horario}hs"

class Contacto(models.Model):
    motivo = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15) 
    email = models.EmailField()
    mensaje = RichTextField(blank=True, null=True) 
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_completo}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=255) 
    imagen = models.ImageField(upload_to='posts', null=True, blank=True)

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="comentarios")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios")
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=255) 

class Mensaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_entrantes")
    fecha = models.DateTimeField(auto_now_add=True)
    asunto = models.CharField(max_length=30)
    contenido = RichTextField(blank=True, null=True) 
    no_leido = models.BooleanField(default=True)
    



    

    
    
   


    




