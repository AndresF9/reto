from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from SalonesEmpresariales.serializer import ClienteSerializer,EventoSerializer
from .models import Cliente,Evento
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import FieldError
#API

#Crud ClientView
class ClientView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset=Cliente.objects.all()

#Crud EventView
class EventView(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset=Evento.objects.all()

#Endpoint para consultar fechas 
@csrf_exempt
def EventFilter(request):
    try:
        if request.method == 'GET':

            return render(request,'fechaFilter.html')
        if request.method == 'POST':
           
           
           if (request.POST.get('fechaI') and request.POST.get('fechaF')):
                fechaInicio=request.POST.get('fechaI')
                fechaFinal=request.POST.get('fechaF')
                objects=Evento.objects.filter(Q(Fecha__gt=fechaInicio) & Q(Fecha__lt=fechaFinal) & Q(Estado='Confirmado'))
                print(objects)
                return render(request,'fechaFilter.html',{'eventos':objects})
           else:
               return render(request,'fechaFilter.html',{'mensaje':'Introduce ambas fechas por favor'})
    except FieldError as e:
        print(e)
        return HttpResponse(400)
