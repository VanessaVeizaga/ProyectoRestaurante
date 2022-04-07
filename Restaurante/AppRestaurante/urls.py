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
]