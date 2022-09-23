from dataclasses import fields
import requests
import os
import json
from dotenv import load_dotenv
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, authentication
from rest_framework import status
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance
from django.core import serializers

from .models import Locales

load_dotenv()

TOKEN = os.getenv('API_TOKEN')


@method_decorator(csrf_exempt, name='dispatch')
class getPlaces(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, query):
        buscarApiDenue = False
        try:
            if not buscarApiDenue:
                print('Antes del POINT')
                coords = request.query_params['proximity'].split(',')
                latitude = coords[0]
                longitud = coords[1]
                lugares = []
                print(type(latitude), type(longitud))
                pnt = 'POINT({} {})'.format(float(longitud), float(latitude))
                point = GEOSGeometry(pnt, srid=4326)
                locales = serializers.serialize('python', Locales.objects.filter(Clase_actividad__contains=query).filter(punto__distance_lte=(point, Distance(m=request.query_params["metros"]))))
                for place in locales:
                    lugares.append(place['fields'])
                if len(lugares) == 0:
                    raise Exception()
                print('--------------------------------------------------   ')
                data = {
                    'message': 'Se encontraron resultados en la Base de Datos',
                    'lugares': lugares
                }
                print('Se buscó en la Base de Datos')
                return Response(data, status=status.HTTP_200_OK)
        except:
            print('ESTOY EN EL EXCEPT')
            try:
                urlApiBusqueda = f'https://www.inegi.org.mx/app/api/denue/v1/consulta/buscar/{query}/{ request.query_params["proximity"] }/{ request.query_params["metros"] }/{TOKEN}'
                print('PROXIMIDAD -> ', request.query_params["proximity"])
                locales = requests.get(urlApiBusqueda)
                print('LOCALES -> ', locales.json())
                for local in locales.json():
                    localExist = Locales.objects.filter(Id=local['Id'])
                    if not localExist.exists():
                        Locales.objects.create(
                            CLEE=local['CLEE'],
                            Id=local['Id'],
                            Nombre=local['Nombre'],
                            Razon_social=local['Razon_social'],
                            Clase_actividad=local['Clase_actividad'].lower(),
                            Estrato=local['Estrato'],
                            Tipo_vialidad=local['Tipo_vialidad'],
                            Calle=local['Calle'],
                            Num_Exterior=local['Num_Exterior'],
                            Num_Interior=local['Num_Interior'],
                            Colonia=local['Colonia'],
                            CP=local['CP'],
                            Ubicacion=local['Ubicacion'],
                            Telefono=local['Telefono'],
                            Correo_e=local['Correo_e'],
                            Sitio_internet=local['Sitio_internet'],
                            Tipo=local['Tipo'],
                            Longitud=local['Longitud'],
                            Latitud=local['Latitud'],
                            CentroComercial=local['CentroComercial'],
                            TipoCentroComercial=local['TipoCentroComercial'],
                            NumLocal=local['NumLocal'],
                        )
                        print('Se ha registrado')
                data = {
                    'message': 'Se encontraron resultados en el API',
                    'lugares': locales.json()
                }
                print('Se buscó en la api de la INEGI')
                return Response(data, status=status.HTTP_200_OK)
            except:
                return Response("No se encontró ningun lugar cerca de ti", status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class getPlace(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            urlApiBusqueda = f'http://www.inegi.org.mx/app/api/denue/v1/consulta/Ficha/{pk}/{TOKEN}'
            locales = requests.get(urlApiBusqueda)
            return Response(locales.json(), status=status.HTTP_200_OK)
        except:
            return Response("No se encontro informacion para ese lugar", status=status.HTTP_400_BAD_REQUEST)
