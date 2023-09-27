from rest_framework import serializers
from .models import Cliente, Evento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields= ('__all__')

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Evento
        fields= ('__all__')