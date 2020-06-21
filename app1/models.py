from django.db import models
from LogAuth.models import Profile


class Producto(models.Model):
	nombre_p = models.CharField(max_length=200)
	fecha_exp = models.DateTimeField('fecha de expiracion')
	tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
	inventario = models.ManyToManyField(Inventario)
	precio = models.IntegerField(default=1)


class DetalleVenta(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
	cantidad_producto = models.IntegerField(default=1)


class Venta(models.Model):
	producto = models.ManyToManyField(Producto)
	hora_venta = models.DateTimeField('hora venta')

class Tipo(models.Model):
	nombre_t = models.CharField(max_length=200)


class Inventario(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)
	hora_act = models.DateTimeField('fecha de actualizacion')

class Carrito(models.Model):
	producto = models.ManyToManyField(Producto)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

