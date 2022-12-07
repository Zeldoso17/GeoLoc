from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombre, apellido, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo!')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombre, apellido, password):
        usuario = self.create_user(
            email,
            username=username,
            nombre=nombre,
            apellido=apellido,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

# ESTE ES EL MODELO DE USUARIOS DE LA APLICACION
class Usuarios(AbstractBaseUser):
    nombre = models.CharField("Nombre", max_length=70)
    apellido = models.CharField("Apellidos", max_length=70)
    username = models.CharField("Nombre de usuario", max_length=50, unique=True)
    email = models.EmailField("Correo Electronico", max_length=254, unique=True)
    telefono = models.CharField("Numero de telefono", max_length=10, null=False, blank=False, unique=True)
    isEmpresa = models.BooleanField(default=False)
    usuario_administrador = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'email']

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
