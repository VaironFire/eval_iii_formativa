from django.urls import path

from mundial_api import views


urlpatterns = [
    path('equipo/', views.listarequipo),
    path('equipo/<int:id>', views.visualizarEquipo),
    path('jugador/editar/<int:id>', views.gestionarJugador)
]