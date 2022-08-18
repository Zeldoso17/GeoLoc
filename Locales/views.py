import json
import requests
import os
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, authentication
from rest_framework import status

from .models import Locales

load_dotenv()

TOKEN = os.getenv('API_TOKEN')


@method_decorator(csrf_exempt, name='dispatch')
class getPlaces(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, query):
        try:
            urlApiBusqueda = f'http://www.inegi.org.mx/app/api/denue/v1/consulta/buscar/{query}/{ request.query_params["proximity"] }/{ request.query_params["metros"] }/{TOKEN}'
            print('PROXIMIDAD -> ', request.query_params["proximity"])
            locales = requests.get(urlApiBusqueda)
            for local in locales.json():
                localExist = Locales.objects.filter(idLocal=local['Id'])
                if not localExist.exists():
                    Locales.objects.create(
                        clee=local['CLEE'],
                        idLocal=local['Id'],
                        nombreLocal=local['Nombre'],
                        razonSocial=local['Razon_social'],
                        nombreActividad=local['Clase_actividad'],
                        Personal=local['Estrato'],
                        tipoVialidad=local['Tipo_vialidad'],
                        nombreVialidad=local['Calle'],
                        numeroExterior=local['Num_Exterior'],
                        numeroInterior=local['Num_Interior'],
                        nombreAsentamiento=local['Colonia'],
                        codigoPostal=local['CP'],
                        Entidad=local['Ubicacion'],
                        Telefono=local['Telefono'],
                        Correo=local['Correo_e'],
                        sitioInternet=local['Sitio_internet'],
                        tipoUnidadEconomica=local['Tipo'],
                        Longitud=local['Longitud'],
                        Latitud=local['Latitud'],
                        centroComercial=local['CentroComercial'],
                        tipoCentroComercial=local['TipoCentroComercial'],
                        numeroLocal=local['NumLocal']
                    )
                    print('Se ha registrado')
            data = {
                'message': 'Se encontraron resultados',
                'lugares': locales.json()
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response("No se encontró ningun lugar cerca de ti", status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class getPlace(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        urlApiBusqueda = f'http://www.inegi.org.mx/app/api/denue/v1/consulta/Ficha/{pk}/{TOKEN}'
        locales = requests.get(urlApiBusqueda)
        return Response(locales.json(), status=status.HTTP_200_OK)
