from math import inf
import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import*
from .forms import*

def inicio(request):
    return render(request, "inicio.html")
    
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
            reservas_coincidentes = Reserva.objects.filter(local__id__contains = id).filter(dia__gte = dia).filter(horario__icontains = horario)
            suma = 0
            for i in reservas_coincidentes:
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

#---------------LOCAL-----------------------------------------------------------------------------------

def local(request):
    locales = Local.objects.order_by('provincia').all()
    return render(request, "local.html", {"locales": locales})      

def agregarLocal(request):
    if request.method == 'POST':
        miFormulario = LocalFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data    
            local = Local(provincia=informacion['provincia'], localidad=informacion['localidad'], direccion=informacion['direccion'], telefono=informacion['telefono'], capacidad=informacion['capacidad'])
            local.save()
            miFormulario = LocalFormulario()
            mensaje = "Se agregó con éxito el local ubicado en: "
            return render(request, "agregarLocal.html", {"miFormulario": miFormulario, "local": local, "mensaje": mensaje })
    else:
        miFormulario = LocalFormulario()        
    return render(request, "agregarLocal.html", {"miFormulario": miFormulario})

def actualizarLocal(request):
    locales = Local.objects.order_by('provincia').all()
    return render(request, "actualizarLocal.html", {"locales": locales})    

def eliminarLocal(request, id):
    local = Local.objects.get(id = id)
    local.delete()
    locales = Local.objects.order_by('provincia').all()
    return render(request, "actualizarLocal.html", {"locales": locales})

def editarLocal(request, id):
    local = Local.objects.get(id = id)
    if request.method == 'POST':
        miFormulario = LocalFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data    
            local.provincia = informacion["provincia"]
            local.localidad = informacion["localidad"]
            local.direccion = informacion["direccion"]
            local.telefono = informacion["telefono"]
            local.capacidad = informacion["capacidad"]
            local.save()
            miFormulario = LocalFormulario()
            mensaje = "Se guardaron correctamente los cambios."
            return render(request, "editarLocal.html", {"miFormulario": miFormulario, "mensaje": mensaje})
    else:
         miFormulario = LocalFormulario(initial={"provincia": local.provincia, "localidad": local.localidad, "direccion": local.direccion, "telefono": local.telefono, "capacidad": local.capacidad})
    return render(request, "editarLocal.html", {"miFormulario": miFormulario, "id": id})

#-------------------------MENÚ-----------------------------------------------------------------------------------

def menu(request):
    menus = Menu.objects.order_by('tipo').all()
    return render(request, "menu.html", {"menus": menus})    

def agregarMenu(request):
    if request.method == 'POST':
        miFormulario = MenuFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data    
            menu = Menu(tipo=informacion['tipo'], nombre=informacion['nombre'], descripcion=informacion['descripcion'], imagen=informacion['imagen'])
            menu.save()
            miFormulario = MenuFormulario()
            mensaje = "Se agregó con éxito el siguiente menú: "
            return render(request, "agregarMenu.html", {"miFormulario": miFormulario, "menu": menu, "mensaje": mensaje })
    else:
        miFormulario = MenuFormulario()        
    return render(request, "agregarMenu.html", {"miFormulario": miFormulario})
        
def actualizarMenu(request):
    menus = Menu.objects.order_by('tipo').all()
    return render(request, "actualizarMenu.html", {"menus": menus})    

def eliminarMenu(request, id):
    menu = Menu.objects.get(id = id)
    menu.delete()
    menus = Menu.objects.order_by('tipo').all()
    return render(request, "actualizarMenu.html", {"menus": menus})

def editarMenu(request, id):
    menu = Menu.objects.get(id = id)
    if request.method == 'POST':
        miFormulario = MenuFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data    
            menu.tipo = informacion["tipo"]
            menu.nombre = informacion["nombre"]
            menu.descripcion = informacion["descripcion"]
            menu.imagen = informacion["imagen"]
            menu.save()
            miFormulario = MenuFormulario()
            mensaje = "Se guardaron correctamente los cambios."
            return render(request, "editarMenu.html", {"miFormulario": miFormulario, "mensaje": mensaje})
    else:
         miFormulario = MenuFormulario(initial={"tipo": menu.tipo, "nombre": menu.nombre, "descripcion": menu.descripcion, "imagen": menu.imagen})
    return render(request, "editarMenu.html", {"miFormulario": miFormulario, "id": id})

    
