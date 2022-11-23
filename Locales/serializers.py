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

class registerPlaceSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=False)
    razonSocial = serializers.CharField(required=False)
    claseActividad = serializers.CharField(required=False)
    estrato = serializers.CharField(required=False)
    tipoVialidad = serializers.CharField(required=False)
    calle = serializers.CharField(required=False)
    numExterior = serializers.CharField(required=False)
    numInterior = serializers.CharField(required=False)
    colonia = serializers.CharField(required=False)
    cp = serializers.CharField(required=False)
    ubicacion = serializers.CharField(required=False)
    telefono = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    sitioWeb = serializers.CharField(required=False)
    tipoEstablecimiento = serializers.CharField(required=False)
    Longitud = serializers.CharField(required=False)
    Latitud = serializers.CharField(required=False)
    centroComercial = serializers.CharField(required=False)
    numLocal = serializers.CharField(required=False)

    def create(self, validated_data):
        instance = Locales()
        instance.Nombre = validated_data.get('nombre')
        instance.Razon_social = validated_data.get('razonSocial')
        instance.Clase_actividad = validated_data.get('claseActividad')
        instance.Estrato = validated_data.get('estrato')
        instance.Tipo_vialidad = validated_data.get('tipoVialidad')
        instance.Calle = validated_data.get('calle')
        instance.Num_Exterior = validated_data.get('numExterior')
        instance.Num_Interior = validated_data.get('numInterior')
        instance.Colonia = validated_data.get('colonia')
        instance.CP = validated_data.get('cp')
        instance.Ubicacion = validated_data.get('ubicacion')
        instance.Telefono = validated_data.get('telefono')
        instance.Correo_e = validated_data.get('email')
        instance.Sitio_internet = validated_data.get('sitioWeb')
        instance.Tipo = validated_data.get('tipoEstablecimiento')
        instance.Longitud = validated_data.get('Longitud')
        instance.Latitud = validated_data.get('Latitud')
        instance.CentroComercial = validated_data.get('centroComercial')
        instance.NumLocal = validated_data.get('numLocal')

        instance.save()
        return instance