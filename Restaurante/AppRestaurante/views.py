from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import*
from .forms import*

def inicio(request):
    return render(request, "inicio.html")

#------------------RESERVA------------------------------------------------------------------------

@login_required    
def reserva(request):
    if request.method == 'POST':
        miFormulario = ReservaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            user = User.objects.get(username = request.user)
            informacion = miFormulario.cleaned_data  
            dia=informacion['dia']
            horario=informacion['horario']
            cantidad_personas=informacion['cantidad_personas']
            local = informacion['local']
            reservas_coincidentes = Reserva.objects.filter(local__id__contains = local.id).filter(dia__gte = dia).filter(horario__icontains = horario)
            suma = 0
            for i in reservas_coincidentes:
                suma += i.cantidad_personas
            if suma + cantidad_personas <= local.capacidad:     
                reserva = Reserva(user = user, dia = dia, horario = horario, cantidad_personas = cantidad_personas, local = local)
                reserva.save()
                miFormulario = ReservaFormulario()
                mensaje = "Se registró con éxito su reserva. ¡Gracias por elegirnos!"
            else:
                mensaje = "No es posible generar una reserva con los datos ingresados. Por favor intente en otra fecha, horario o local."
            return render(request, "reserva.html", {"miFormulario": miFormulario, "mensaje": mensaje})    
    else:
        miFormulario = ReservaFormulario()
    return render(request, "reserva.html", {"miFormulario": miFormulario})

@login_required
def eliminarReserva(request, id):  
    reserva = Reserva.objects.get(id = id)
    reserva.delete()
    return render(request, "miCuenta.html")
    
#--------------------CONTACTO----------------------------------------------------------------------------------

def contacto(request):
    if request.method == 'POST':       
        miFormulario = ContactoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data    
            contacto = Contacto(motivo=informacion['motivo'], nombre_completo=informacion['nombre_completo'], telefono=informacion['telefono'], email=informacion['email'], mensaje=informacion['mensaje'], local=informacion['local'])
            contacto.save()
            miFormulario = ContactoFormulario()

            motivo = request.POST['motivo']
            mensaje = request.POST['mensaje'] + " " + request.POST['email']
            remitente = settings.EMAIL_HOST_USER
            destinatario = ["vanessaveizaga@gmail.com"]
            send_mail(motivo, mensaje, remitente, destinatario)
            message = "¡Tu mensaje ha sido enviado exitosamente!"
            return render(request, "contacto.html", {"miFormulario": miFormulario, "mensaje": message})
    else:
        miFormulario = ContactoFormulario()
    return render(request, "contacto.html", {"miFormulario": miFormulario})

#---------------LOCAL-----------------------------------------------------------------------------------
 
def local(request):
    provincias = set()
    locales = Local.objects.all()
    for local in locales:
        provincias.add(local.provincia)
    provincias = sorted(list(provincias))
    return render(request, "local.html", {"locales": locales, "provincias": provincias})  

@login_required
def agregarLocal(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            miFormulario = LocalFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data    
                local = Local(provincia=informacion['provincia'], localidad=informacion['localidad'], direccion=informacion['direccion'], telefono=informacion['telefono'], capacidad=informacion['capacidad'], imagen=informacion['imagen'])
                local.save()
                miFormulario = LocalFormulario()
                mensaje = "Se agregó con éxito el local ubicado en: "
                return render(request, "agregarLocal.html", {"miFormulario": miFormulario, "local": local, "mensaje": mensaje })
        else:
            miFormulario = LocalFormulario()        
        return render(request, "agregarLocal.html", {"miFormulario": miFormulario})
    else:
         return render(request, "sin_acceso.html", {"mensaje": "No tiene permiso de acceso a este sitio."})

@login_required
def eliminarLocal(request, id):
    local = Local.objects.get(id = id)
    local.delete()
    provincias = set()
    locales = Local.objects.all()
    for local in locales:
        provincias.add(local.provincia)
    provincias = sorted(list(provincias))
    return render(request, "local.html", {"locales": locales, "provincias": provincias})

@login_required
def editarLocal(request, id):
    if request.user.is_superuser:
        local = Local.objects.get(id = id)
        if request.method == 'POST':
            miFormulario = LocalFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data    
                local.provincia = informacion["provincia"]
                local.localidad = informacion["localidad"]
                local.direccion = informacion["direccion"]
                local.telefono = informacion["telefono"]
                local.capacidad = informacion["capacidad"]
                local.imagen = informacion["imagen"]
                local.save()
                miFormulario = LocalFormulario()
                mensaje = "Se guardaron correctamente los cambios."
                return render(request, "editarLocal.html", {"miFormulario": miFormulario, "mensaje": mensaje})
        else:
            miFormulario = LocalFormulario(initial={"provincia": local.provincia, "localidad": local.localidad, "direccion": local.direccion, "telefono": local.telefono, "capacidad": local.capacidad, "imagen": local.imagen})
        return render(request, "editarLocal.html", {"miFormulario": miFormulario, "id": id})
    else:
        return render(request, "sin_acceso.html", {"mensaje": "No tiene permiso de acceso a este sitio."})

#-------------------------MENÚ-----------------------------------------------------------------------------------

def menu(request):
    tipos = set()
    menus = Menu.objects.all()
    for menu in menus:
        tipos.add(menu.tipo)
    tipos = sorted(list(tipos))
    return render(request, "menu.html", {"menus": menus, "tipos": tipos})    

@login_required
def agregarMenu(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            miFormulario = MenuFormulario(request.POST, request.FILES)
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
    else:
        return render(request, "sin_acceso.html", {"mensaje": "No tiene permiso de acceso a este sitio."})

@login_required               
def eliminarMenu(request, id):
    menu = Menu.objects.get(id = id)
    menu.delete()
    tipos = set()
    menus = Menu.objects.all()
    for menu in menus:
        tipos.add(menu.tipo)
    tipos = sorted(list(tipos))
    return render(request, "menu.html", {"menus": menus, "tipos": tipos})

@login_required
def editarMenu(request, id):
    if request.user.is_superuser:
        menu = Menu.objects.get(id = id)
        if request.method == 'POST':
            miFormulario = MenuFormulario(request.POST, request.FILES)
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
    else:
        return render(request, "sin_acceso.html", {"mensaje": "No tiene permiso de acceso a este sitio."})
  #--------------------LOGIN------------------------------------------------------------------------

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje": f"¡Bienvenido/a {username}!"})
            else:
                return render(request, "login.html", {"mensaje": "Error, datos incorrectos.", "form": form})   
        else:
            return render(request, "login.html", {"mensaje": "Error, formulario erróneo", "form": form})   
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})              

def register(request):
    if request.method == "POST":
        miFormulario = UserRegisterForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            username = miFormulario.cleaned_data['username']
            miFormulario.save()
            return render(request, "inicio.html", {"miFormulario": miFormulario, "mensaje": "¡Te has registrado con éxito!"})
    else:
        miFormulario = UserRegisterForm()
    return render(request, "registro.html", {"miFormulario": miFormulario})    

#-------------------------PERFIL-----------------------------------------------------------------

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            if informacion['imagen'] == False:
                usuario.imagen = 'avatar/perfil.png'
            else:    
                usuario.imagen = informacion['imagen']
            usuario.save()
            miFormulario = UserEditForm()
            return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "mensaje": "Se guardaron los cambios correctamente."})
    else:
        miFormulario = UserEditForm(initial={"first_name": usuario.first_name, "last_name": usuario.last_name, "email": usuario.email, "imagen": usuario.imagen})
    return render(request, "editarPerfil.html", {"miFormulario": miFormulario})    

@login_required
def miCuenta(request):
    perfil = User.objects.get(username = request.user)
    mensajes = len(Mensaje.objects.filter(destinatario = request.user).filter(no_leido = True))
    return render(request, "miCuenta.html", {"perfil": perfil, "mensajes": mensajes})    

#---------------------COMUNIDAD-----------------------------------------------------

def comunidad(request):
    posts = Post.objects.order_by('-fecha').all()
    if request.method == 'POST':
        miFormulario = PostFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            user = User.objects.get(username = request.user)
            informacion = miFormulario.cleaned_data    
            post = Post(user=user, contenido=informacion['contenido'], imagen=informacion['imagen'])
            post.save()
            miFormulario = PostFormulario()
            return redirect('Comunidad')           
    else:   
        miFormulario = PostFormulario()     
    return render(request, "comunidad.html", {"miFormulario": miFormulario, "posts": posts})         

@login_required
def comentario(request, id_post):
    if request.method == "POST":
        miFormulario = ComentarioFormulario(request.POST)
        if miFormulario.is_valid():
            user = User.objects.get(username = request.user)
            post = Post.objects.get(id = id_post)
            comentario = Comentario(user = user, post = post, contenido = miFormulario.cleaned_data['contenido'])
            comentario.save()
            mensaje = "¡Tu comentario ha sido agregado con éxito!"
            return render(request, "comentario.html", {"miFormulario": miFormulario, "comentario":comentario, "mensaje": mensaje} )
    else:
        miFormulario = ComentarioFormulario()
    return render(request, "comentario.html", {"miFormulario": miFormulario})    

@login_required
def eliminarComentario(request, id):
    comentario = Comentario.objects.get(id = id)
    comentario.delete()
    return redirect('Comunidad')

@login_required
def editarComentario(request, id):
    comentario = Comentario.objects.get(id = id)
    if request.user == comentario.user or request.user.is_superuser:
        if request.method == 'POST':
            miFormulario = ComentarioFormulario(request.POST)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data    
                comentario.contenido = informacion["contenido"]
                comentario.save()
                miFormulario = ComentarioFormulario()
                mensaje = "¡Tu comentario fue modificado correctamente!."
                return render(request, "editarComentario.html", {"miFormulario": miFormulario, "mensaje": mensaje})
        else:
            miFormulario = ComentarioFormulario(initial={"contenido": comentario.contenido})
        return render(request, "editarComentario.html", {"miFormulario": miFormulario}) 
    else:
        return render(request, "sin_acceso.html", {"mensaje": "No tiene permiso de acceso a este sitio."})

@login_required
def eliminarPost(request, id):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('Comunidad')

@login_required
def editarPost(request, id):
    post = Post.objects.get(id = id)
    if request.user == post.user or request.user.is_superuser:
        if request.method == 'POST':
            miFormulario = PostFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data    
                post.contenido = informacion["contenido"]
                if informacion['imagen'] == False:
                    post.imagen = None     
                else:
                    post.imagen = informacion['imagen'] 
                post.save()
                miFormulario = PostFormulario()
                mensaje = "¡Tu post fue modificado correctamente!."
                return render(request, "editarPost.html", {"miFormulario": miFormulario, "mensaje": mensaje})
        else:
            miFormulario = PostFormulario(initial={"contenido": post.contenido, "imagen": post.imagen})
        return render(request, "editarPost.html", {"miFormulario": miFormulario})   
    else:
        return render(request, "sin_acceso.html", {"mensaje": "No tiene permiso de acceso a este sitio."})

def detallePost(request, id):
    post = Post.objects.get(id = id)
    return render(request, "detallePost.html", {"post": post})  

@login_required
def mensaje(request, id_destinatario):
    if request.method == "POST":
        miFormulario = MensajeFormulario(request.POST)
        if miFormulario.is_valid():
            user = User.objects.get(username = request.user)
            global destinatario
            destinatario = User.objects.get(id = id_destinatario)
            mensaje = Mensaje(user = user, destinatario = destinatario, asunto = miFormulario.cleaned_data['asunto'], contenido = miFormulario.cleaned_data['contenido'])
            mensaje.save()
            miFormulario = MensajeFormulario(request.POST)
            mensaje = "¡Tu mensaje se ha enviado exitosamente!"
            return render(request, "mensaje.html", {"destinatario": destinatario, "miFormulario": miFormulario, "mensaje": mensaje}) 
    else:
        miFormulario = MensajeFormulario()
        destinatario = User.objects.get(id = id_destinatario)
    return render(request, "mensaje.html", {"miFormulario": miFormulario, "destinatario": destinatario})  

@login_required
def perfil(request, id_user):
    perfil = User.objects.get(id = id_user)
    return render(request, "perfil.html", {"perfil": perfil})  

@login_required
def buzon(request, id_user):
    recibidos = Mensaje.objects.order_by('-fecha').filter(destinatario = id_user)
    enviados = Mensaje.objects.order_by('-fecha').filter(user = id_user)
    return render(request, "buzon.html", {"recibidos": recibidos, "enviados": enviados})  

@login_required
def leerMensaje(request, id):
    mensaje = Mensaje.objects.get(id = id)
    mensaje.no_leido = False
    mensaje.save()
    return render(request, "leerMensaje.html", {"mensaje": mensaje})  

def about_us(request):
    ramiro = '/media/about_us/Ramiro.jpg'
    vane = '/media/about_us/Vane.jpg'
    print(vane)
    return render(request, "about_us.html", {"ramiro": ramiro, "vane": vane})      
