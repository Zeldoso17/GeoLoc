from dataclasses import fields
from rest_framework import serializers
from .models import Locales

class CustomFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Locales
        fields = '__all__'

class getClaseActividadValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Locales
        fields = ['Clase_actividad']