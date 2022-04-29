from django.urls import path
from AppRestaurante import views

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

]