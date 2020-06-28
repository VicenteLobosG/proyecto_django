from django.db import models
from LogAuth.models import Profile




class Producto(models.Model):
	nombre_p = models.CharField(max_length=200)
	fecha_exp = models.DateTimeField('fecha de expiracion')
	precio = models.IntegerField(default=1)
	foto = models.ImageField(upload_to='fotos', blank=True, null=True)

class Inventario(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)
	hora_act = models.DateTimeField('fecha de actualizacion')


class Venta(models.Model):
	hora_venta = models.DateTimeField('hora venta')
	total = models.IntegerField(default=0)


class OrdenCompra(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad_producto = models.IntegerField(default=1)
	total = models.IntegerField(default=1)

class Carrito(models.Model):
	orden = models.ManyToManyField(OrdenCompra, null=True, blank=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True, blank=True)
	activo = models.BooleanField(default=True)

