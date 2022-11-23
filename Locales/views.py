import requests
import os
from dotenv import load_dotenv
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, authentication
from rest_framework import status
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance
from django.core import serializers

from .models import Locales
from .serializers import (CustomFilterSerializer, getClaseActividadValuesSerializer, registerPlaceSerializer)

load_dotenv()

TOKEN = os.getenv('API_TOKEN')
METROS = []
METROS_ACTUAL = ''
METROS_PREVIOS = ''

@method_decorator(csrf_exempt, name='dispatch')
class getPlaces(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, query):
        buscarApiDenue = False
        try:
            if not buscarApiDenue:
                print('HOLA JEJEJEJE')
                coords = request.query_params['proximity'].split(',')
                print('COORDS')
                METROS_ACTUAL = request.query_params["metros"]
                print('METROS ACTUALES')
                METROS.append(METROS_ACTUAL)
                print('AGREGAR METROS A ARRAY')
                if len(METROS) > 1:
                    METROS_PREVIOS = METROS[-1-1]
                print('OBTENER LOS METROS PREVIOS')
                print('METROS ACTUALES -> ', METROS_ACTUAL)
                #print('METROS PREVIOS -> ', METROS_PREVIOS)
                latitude = coords[0]
                longitud = coords[1]
                lugares = []
                pnt = 'POINT({} {})'.format(float(longitud), float(latitude))
                point = GEOSGeometry(pnt, srid=4326)
                print('ANTES DE LOS LOCALESBD JEJE')
                locales = serializers.serialize('python', Locales.objects.filter(Clase_actividad__icontains=query).filter(punto__distance_lte=(point, Distance(m=request.query_params["metros"]))))
                for place in locales:
                    lugares.append(place['fields'])
                if len(lugares) == 0:
                    print('ENTRO AL IF PARA VERIFICAR QUE NO HAY RESULTADOS')
                    raise Exception()
                
                if int(METROS_ACTUAL) > int(METROS_PREVIOS):
                    print('ENTRO AL IF PARA VERIFICAR LOS METROS')
                print('-------------------------------------------------------------------------------------------------------------------')
                data = {
                    'message': 'Se encontraron resultados en la Base de Datos',
                    'lugares': lugares
                }
                print('Se buscó en la Base de Datos')
                return Response(data, status=status.HTTP_200_OK)
        except:
            try:
                urlApiBusqueda = f'https://www.inegi.org.mx/app/api/denue/v1/consulta/buscar/{query}/{ request.query_params["proximity"] }/{ request.query_params["metros"] }/{TOKEN}'
                print('PROXIMIDAD -> ', request.query_params["proximity"])
                locales = requests.get(urlApiBusqueda)
                print('LOCALES INEGI -> ', locales.json())
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
class getPlaceInfo(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        """
        lugares = []
        try:
            locales = serializers.serialize('python',Locales.objects.filter(Id=pk))
            for place in locales:
                    lugares.append(place['fields'])
            data = {
                'message': 'Se obtuvo un resultado',
                'local': lugares[0]
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response("No se encontro informacion para ese lugar", status=status.HTTP_400_BAD_REQUEST)
        """
        try:
            urlApiBusqueda = f'http://www.inegi.org.mx/app/api/denue/v1/consulta/Ficha/{pk}/{TOKEN}'
            locales = requests.get(urlApiBusqueda)
            return Response(locales.json(), status=status.HTTP_200_OK)
        except:
            return Response("No se encontro informacion para ese lugar", status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name="dispatch")
class getPlace(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Locales.objects.all()

        Nombre = self.request.query_params.get('Nombre', None)
        Clase_actividad = self.request.query_params.get('Clase_actividad', None)
        Calle = self.request.query_params.get('Calle', None)
        Colonia = self.request.query_params.get('Colonia', None)
        CP = self.request.query_params.get('CP', None)
        Ubicacion = self.request.query_params.get('Ubicacion', None)

        """ Condicional para si hay un query param llamado Nombre """
        if Nombre:
            queryset = queryset.filter(Nombre=Nombre)
        
        """ Condicional para si hay un query param llamado Clase_actividad """
        if Clase_actividad:
            queryset = queryset.filter(Clase_actividad=Clase_actividad)
        
        """ Condicional para si hay un query param llamado Calle """
        if Calle:
            queryset = queryset.filter(Calle=Calle)
        
        """ Condicional para si hay un query param llamado Colonia """
        if Colonia:
            queryset = queryset.filter(Colonia=Colonia)
        
        """ Condicional para si hay un query param llamado CP """
        if CP:
            queryset = queryset.filter(CP=CP)
        
        """ Condicional para si hay un query param llamado Ubicacion """
        if Ubicacion:
            queryset = queryset.filter(Ubicacion=Ubicacion)
        
        serializer = CustomFilterSerializer(queryset, many=True)

        data = {
            'message': 'Success',
            'data': serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class getClaseActividadValues(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        values = Locales.objects.all().distinct('Clase_actividad')
        
        serializer = getClaseActividadValuesSerializer(values, many=True)

        data = {
            'message': 'Success',
            'data': serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
class registerPlace(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if request.method == 'POST':
            print("Antes del data")
            local = Locales.objects.create(
                Nombre = request.data['nombre'],
                Razon_social = request.data['razonSocial'],
                Clase_actividad = request.data['claseActividad'],
                Estrato = request.data['estrato'],
                Tipo_vialidad = request.data['tipoVialidad'],
                Calle = request.data['calle'],
                Num_Exterior = request.data['numExterior'],
                Num_Interior = request.data['numInterior'],
                Colonia = request.data['colonia'],
                CP = request.data['cp'],
                Ubicacion = request.data['ubicacion'],
                Telefono = request.data['telefono'],
                Correo_e = request.data['email'],
                Sitio_internet = request.data['sitioWeb'],
                Tipo = request.data['tipoEstablecimiento'],
                Longitud = request.data['Longitud'],
                Latitud = request.data['Latitud'],
                CentroComercial = request.data['centroComercial'],
                NumLocal = request.data['numLocal']
            )
            local.save()
            return Response({'message': "Lugar registrado exitosamente"}, status=status.HTTP_200_OK)
        return Response({'error', 'Algo fué mal'}, status=status.HTTP_400_BAD_REQUEST)