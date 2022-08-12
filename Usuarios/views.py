from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuarios
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, UserModelSerializer, UserLoginSerializer
from rest_framework import status, permissions, authentication
from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout, login
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils.decorators import method_decorator



# VISTA PARA CREAR USUARIOS
@method_decorator(csrf_exempt, name='dispatch')
class CreateUser(APIView):
    # AQUI LE DECIMOS A LA VISTA QUE PERMITA TODO
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        # AQUI LE PASAMOS LOS DATOS QUE VIENEN DEL FRONTEND AL SERIALIZADOR
        serializer = UserSerializer(data=request.data)
        print("DATA -> ", request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'Tienes que llenar todos los campos', "error": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Error al crear usuario'}, status = status.HTTP_400_BAD_REQUEST)

# VISTA PARA EL LOGIN DE USUARIOS
@method_decorator(csrf_exempt, name='dispatch')
class LoginUser(APIView):
    # AQUI LE DECIMOS A LA VISTA QUE PERMITA TODO
    permission_classes = (permissions.AllowAny,) 
    # authentication_classes = (authentication.TokenAuthentication,)

    queryset = Usuarios.objects.filter(activo=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['POST'])
    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user, token = serializer.save()
            login(request, user)
            data = {
                'user': UserModelSerializer(user).data,
                'access_token': token
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'message':'Necesitas una cuenta para iniciar sesión'}, status=status.HTTP_400_BAD_REQUEST)

# VISTA PARA CERRAR SESION
class LogoutUser(APIView):
    # AQUI PROTEGEMOS LA VISTA PARA QUE SOLO USUARIOS VALIDOS PUEDAN ACCEDER
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            # Aqui eliminamos el token que se genero para el usuario
            request.user.auth_token.delete()
            logout(request)
            return Response({'success':'Has cerrado sesión correctamente'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Algo fue mal durante el logout'}, status=status.HTTP_400_BAD_REQUEST)

# VISTA PARA OBTENER EL CSRF TOKEN
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'succes': 'CSRF cookie set'})