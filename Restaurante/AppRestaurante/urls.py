from django.urls import path
from AppRestaurante import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('menu/', views.menu, name="Menu"),
    path('local/', views.local, name="Local"),
    path('reserva/', views.reserva, name="Reserva"),
    path('contacto/', views.contacto, name="Contacto"),
    path('busquedaLocal/', views.busquedaLocal, name="BusquedaLocal"),
    path('buscar/', views.buscar, name="Buscar"),
    path('actualizarLocal/', views.actualizarLocal, name="ActualizarLocal"),
    path('agregarLocal/', views.agregarLocal, name="AgregarLocal"),
    path('eliminarLocal/<id>', views.eliminarLocal, name="EliminarLocal"),
    path('editarLocal/<id>', views.editarLocal, name="EditarLocal"),
    path('actualizarMenu', views.actualizarMenu, name="ActualizarMenu"),
    path('agregarMenu/', views.agregarMenu, name="AgregarMenu"),
    path('eliminarMenu/<id>', views.eliminarMenu, name="EliminarMenu"),
    path('editarMenu/<id>', views.editarMenu, name="EditarMenu"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    path('miCuenta', views.miCuenta, name="MiCuenta"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('comunidad', views.comunidad, name="Comunidad"),
    path('comentario/<id_post>', views.comentario, name="Comentario"),
    path('eliminarComentario/<id>', views.eliminarComentario, name="EliminarComentario"),
    path('editarComentario/<id>', views.editarComentario, name="EditarComentario"),
    path('eliminarPost/<id>', views.eliminarPost, name="EliminarPost"),
    path('editarPost/<id>', views.editarPost, name="EditarPost"),
    path('eliminarReserva/<id>', views.eliminarReserva, name="EliminarReserva"),
    path('detallePost/<id>', views.detallePost, name="DetallePost"),
    path('perfil/<id_user>', views.perfil, name="Perfil"),
    path('mensaje/<id_destinatario>', views.mensaje, name="Mensaje"),


]