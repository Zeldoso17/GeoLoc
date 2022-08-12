import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, authentication

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class listadoLocales(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        token = '5177aa88-830c-46bf-bf79-c3e979855634'
        urlApiBusqueda = f'http://www.inegi.org.mx/app/api/denue/v1/consulta/buscar/comida/32.493689,-116.933057/600/{token}'
        locales = requests.get(urlApiBusqueda)
        return Response(locales.json())

@method_decorator(csrf_exempt, name='dispatch')
class obtenerLocal(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
         token = '5177aa88-830c-46bf-bf79-c3e979855634'
         urlApiBusqueda = f'http://www.inegi.org.mx/app/api/denue/v1/consulta/Ficha/8112768/{token}'
         locales = requests.get(urlApiBusqueda)
         return Response(locales.json())