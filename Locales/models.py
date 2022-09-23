from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField

# Create your models here.

class Locales(models.Model):
    CLEE = models.CharField("CLEE", max_length=200, blank=True, null=True)
    Id = models.CharField(("Id del local"), max_length=50, blank=True, null=True)
    Nombre = models.CharField(("Nombre del local"), max_length=200, blank=True, null=True)
    Razon_social = models.CharField(("Razon social"), max_length=200, blank=True, null=True)
    Clase_actividad = models.CharField(("Nombre de la actividad"), max_length=200, blank=True, null=True)
    Estrato = models.CharField(("Personal ocupado"), max_length=50, blank=True, null=True)
    Tipo_vialidad = models.CharField(("Tipo de Vialidad"), max_length=50, blank=True, null=True)
    Calle = models.CharField(("Nombre de la vialidad"), max_length=100, blank=True, null=True)
    Num_Exterior = models.CharField(("Numero Exterior"), max_length=50, blank=True, null=True)
    Num_Interior = models.CharField(("Numero Interior"), max_length=50, blank=True, null=True)
    Colonia = models.CharField(("Nombre del Asentamiento Humano"), max_length=50, blank=True, null=True)
    CP = models.CharField(("Codigo Postal"), max_length=50, blank=True, null=True)
    Ubicacion = models.CharField(("Entidad"), max_length=50, blank=True, null=True)
    Telefono = models.CharField(("Numero de Telefono"), max_length=50, blank=True, null=True)
    Correo_e = models.CharField(("Correo Electronico"), max_length=100, blank=True, null=True)
    Sitio_internet = models.CharField(("Sitio de Internet"), max_length=50, blank=True, null=True)
    Tipo = models.CharField(("Tipo de unidad Economica"), max_length=50, blank=True, null=True)
    Longitud = models.CharField(("Longitud"), max_length=100, blank=True, null=True)
    Latitud = models.CharField(("Latitud"), max_length=50)
    CentroComercial = models.CharField(("Centro Comercial"), max_length=200, blank=True, null=True)
    TipoCentroComercial = models.CharField(("Tipo de Centro Comercial"), max_length=100, blank=True, null=True)
    NumLocal = models.CharField(("Numero de Local"), max_length=50, blank=True, null=True)
    punto = PointField(blank=True, null=True, srid=4326)

    def save(self, *args, **kwargs):
        self.punto = Point(float(self.Longitud), float(self.Latitud))
        super(Locales, self).save(*args, **kwargs)

