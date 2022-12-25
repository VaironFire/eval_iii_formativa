from django.shortcuts import render
from mundial_api.models import Equipo, Jugador
# Create your views here.
def ListarEquipos(request):
    equipos=Equipo.objects.all()
    return render(request,'mundial_app/listadoequipos.html',{"equipos":equipos})

def MostrarEquipo(request, id):
    equipo=Equipo.objects.filter(id=id).first()
    return render(request,'mundial_app/Mostrarequipo.html',{"equipo":equipo})