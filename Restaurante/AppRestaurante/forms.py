from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Local

class MenuFormulario(forms.Form):
    opciones = (("Entradas","Entradas"), ("Platos principales","Platos Principales"), ("Postres","Postres"), ("Desayuno-Merienda","Desayuno-Merienda"))
    tipo = forms.ChoiceField(choices= opciones)
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(label="Descripción", max_length=128) 
    imagen = forms.ImageField()

class LocalFormulario(forms.Form):
    provincia = forms.CharField(max_length=20)
    localidad = forms.CharField(max_length=30)
    direccion = forms.CharField(label="Dirección", max_length=40) 
    telefono = forms.IntegerField(label="Teléfono")   
    capacidad = forms.IntegerField(label="Capacidad", widget= forms.TextInput(attrs={'placeholder':'Cantidad de reservas'}))  
    imagen = forms.ImageField()
    
class ReservaFormulario(forms.Form):
    horarios = opciones = (("10:00","10:00"), ("12:00","12:00"), ("14:00","14:00"), ("16:00","16:00"), ("18:00","18:00"), ("20:00","20:00"), ("22:00","22:00"))
    dia = forms.DateField(label="Fecha", widget= forms.TextInput(attrs={'type':'date'}))
    horario = forms.ChoiceField(choices=horarios)
    cantidad_personas = forms.IntegerField(label="N° de personas", min_value=1)
    local = forms.ModelChoiceField(queryset=Local.objects.all())

class ContactoFormulario(forms.Form):
    motivo = forms.ChoiceField(choices=(("Consulta","Consulta"), ("Sugerencia","Sugerencia"), ("Reclamo","Reclamo")))
    nombre_completo = forms.CharField(max_length=50)
    telefono = forms.IntegerField(label="Teléfono") 
    email = forms.EmailField(max_length=30)
    mensaje = forms.CharField(max_length=256)
    local = forms.ModelChoiceField(queryset=Local.objects.all(), required=False)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "E-mail")
    first_name = forms.CharField(label = "Nombre")
    last_name = forms.CharField(label = "Apellido")
    imagen = forms.ImageField(label="Foto")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)  
    imagen = forms.ImageField(label="Foto", required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'imagen', 'password1', 'password2']
        help_texts = {k:"" for k in fields}  

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = "Modificar e-mail:")
    first_name = forms.CharField(label = "Modificar nombre")
    last_name = forms.CharField(label = "Modificar apellido")
    imagen = forms.ImageField(label="Modificar foto", required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)  
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'imagen']
        help_texts = {k:"" for k in fields}  

class PostFormulario(forms.Form):
    contenido = forms.CharField(widget=forms.Textarea, label="Escribe aquí")
    imagen = forms.ImageField(label="Puedes compartir una foto aquí", required=False)

class ComentarioFormulario(forms.Form):    
    contenido = forms.CharField(widget=forms.Textarea)

class MensajeFormulario(forms.Form):    
    asunto = forms.CharField(max_length=30)
    contenido = forms.CharField(widget=forms.Textarea)
    no_leido = forms.BooleanField(required=False)