from django.http import HttpResponse
from django.shortcuts import render
from .models import*
from .forms import*

def inicio(request):
    return render(request, "inicio.html")
    
def menu(request):
    if request.method == 'POST':
        miFormulario = MenuFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data    
            menu = Menu(tipo=informacion['tipo'], nombre=informacion['nombre'], descripcion=informacion['descripcion'])
            menu.save()
            return render(request, "inicio.html")
    else:
        miFormulario = MenuFormulario()
    return render(request, "menu.html", {"miFormulario": miFormulario})

def local(request):
    if request.method == 'POST':
        miFormulario = LocalFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data    
            local = Local(provincia=informacion['provincia'], localidad=informacion['localidad'], direccion=informacion['direccion'], telefono=informacion['telefono'], capacidad=informacion['capacidad'])
            local.save()
            return render(request, "inicio.html")
    else:
        miFormulario = LocalFormulario() 
    return render(request, "local.html", {"miFormulario": miFormulario})

def reserva(request):
    if request.method == 'POST':
        miFormulario = ReservaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data  
            nombre_completo=informacion['nombre_completo'] 
            dia=informacion['dia']
            horario=informacion['horario']
            cantidad_personas=informacion['cantidad_personas']
            local = informacion['local']
            id = local.id
            print("--------------------------------------------------------------------------------")  
            reservas = Reserva.objects.filter(local__id__contains = id).filter(dia__gte = dia).filter(horario__icontains = horario)
            print(reservas)
            suma = 0
            for i in reservas:
                suma += i.cantidad_personas
            if suma + cantidad_personas <= local.capacidad:     
                reserva = Reserva(nombre_completo = nombre_completo, dia = dia, horario = horario, cantidad_personas = cantidad_personas, local = local)
                reserva.save()
                miFormulario = ReservaFormulario()
                mensaje = "Se registró con éxito su reserva. ¡Gracias por elegirnos!"
            else:
                mensaje = "No es posible generar una reserva con los datos ingresados. Por favor intente en otra fecha, horario o local."
            return render(request, "reserva.html", {"miFormulario": miFormulario, "mensaje": mensaje})    
    else:
        miFormulario = ReservaFormulario()
    return render(request, "reserva.html", {"miFormulario": miFormulario})

def contacto(request):
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data    
            contacto = Contacto(motivo=informacion['motivo'], nombre_completo=informacion['nombre_completo'], telefono=informacion['telefono'], email=informacion['email'], mensaje=informacion['mensaje'], local=informacion['local'])
            contacto.save()
            return render(request, "inicio.html")
    else:
        miFormulario = ContactoFormulario()
    return render(request, "contacto.html", {"miFormulario": miFormulario})

def busquedaLocal(request):
    return render(request, "busquedaLocal.html") 

def buscar(request):
    if request.GET["provincia"]:
        provincia = request.GET["provincia"]
        locales = Local.objects.filter(provincia__icontains = provincia)
        return render(request, "resultadoBusqueda.html", {"locales": locales, "provincia": provincia})
    else:
      return HttpResponse("No enviaste datos") 

def disponibilidad(reserva):
    locales = Reserva.objects.filter(reserva.local)    
    return locales  

#def disponibilidad(local, dia, horario, cantidad_personas, reservas):
   


        

    
