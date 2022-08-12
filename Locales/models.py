from django.db import models

# Create your models here.

class Locales(models.Model):
    idLocal = models.CharField(("Id del local"), max_length=50, blank=True, null=True)
    nombreLocal = models.CharField(("Nombre del local"), max_length=200, blank=True, null=True)
    razonSocial = models.CharField(("Razon social"), max_length=200, blank=True, null=True)
    nombreActividad = models.CharField(("Nombre de la actividad"), max_length=200, blank=True, null=True)
    Personal = models.CharField(("Personal ocupado"), max_length=50, blank=True, null=True)
    tipoVialidad = models.CharField(("Tipo de Vialidad"), max_length=50, blank=True, null=True)
    nombreVialidad = models.CharField(("Nombre de la vialidad"), max_length=100, blank=True, null=True)
    numeroExterior = models.CharField(("Numero Exterior"), max_length=50, blank=True, null=True)
    numeroInterior = models.CharField(("Numero Interior"), max_length=50, blank=True, null=True)
    nombreAsentamiento = models.CharField(("Nombre del Asentamiento Humano"), max_length=50, blank=True, null=True)
    codigoPostal = models.CharField(("Codigo Postal"), max_length=50, blank=True, null=True)
    Entidad = models.CharField(("Entidad"), max_length=50, blank=True, null=True)
    Telefono = models.CharField(("Numero de Telefono"), max_length=50, blank=True, null=True)
    Correo = models.CharField(("Correo Electronico"), max_length=100, blank=True, null=True)
    sitioInternet = models.CharField(("Sitio de Internet"), max_length=50, blank=True, null=True)
    tipoUnidadEconomica = models.CharField(("Tipo de unidad Economica"), max_length=50, blank=True, null=True)
    Latitud = models.CharField(("Latitud"), max_length=100, blank=True, null=True)
    Longitud = models.CharField(("Longitud"), max_length=50),
    centroComercial = models.CharField(("Centro Comercial"), max_length=200, blank=True, null=True)
    tipoCentroComercial = models.CharField(("Tipo de Centro Comercial"), max_length=100, blank=True, null=True)
    numeroLocal = models.CharField(("Numero de Local"), max_length=50, blank=True, null=True)

