from django.contrib import admin
from app1.models import Producto, DetalleVenta, Venta, Inventario, Carrito
# Register your models here.


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	pass


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
	pass

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
	pass

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
	pass

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
	pass