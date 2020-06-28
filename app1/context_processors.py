from .models import Carrito



"""class Carrito(models.Model):
	orden = models.ManyToManyField(OrdenCompra, null=True, blank=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True, blank=True)
	activo = models.BooleanField(default=True)"""

def carritoglobal(request):
	#var = {}

	data = {}

	if request.user.is_authenticated:
		if request.user.is_superuser == False:
			print("########################################################")
			var = {}
			var['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)
			OC = var['carrito'].orden.all()
			data = {
			        	'OC': OC,
			        }
			return data

		else:
			return {}
	else:
		return {}
			#ES TERRIBLMENTE IMPORTANTE DEVOLVER UN DICCIONARIO VACIO, SI NO, CRASHEA TODO EL SISTEMA
			##########################################################################################


