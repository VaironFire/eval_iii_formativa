from os import stat
from django.shortcuts import render
from django.http import JsonResponse
from mundial_api.models import Equipo, Jugador
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import EquipoSerializer, JugadorSerializer
from mundial_api import serializers
# Create your views here.
@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def listarequipo(request):
    equipo = Equipo.objects.all()
    serializado = EquipoSerializer(equipo, many=True)
    return Response(serializado.data)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def visualizarEquipo(request, id):
    try:
        equipo = Equipo.objects.get(id=id)
        serializado = EquipoSerializer(equipo)
        jugador= Jugador.objects.all()
        serializado = JugadorSerializer(jugador, many=True)
        return Response(serializado.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['PATCH', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def gestionarJugador(request, id):
    #modificar
    if request.method == 'PATCH':
        try:
            jugador = Jugador.objects.get(id=id)
            serializador = JugadorSerializer(jugador, data=request.data, partial=True)
            if serializador.is_valid():
                serializador.save()
                return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #si deseo eliminar 
    if request.method == 'DELETE':
        #hago eliminación
        try:
            jugador = Jugador.objects.get(id=id)
            jugador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    #si deseo ingresar
    if request.method == 'POST':
        try:
            serializador = JugadorSerializer(data=request.data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)    
        except:
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)