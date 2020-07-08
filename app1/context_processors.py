from .models import Carrito
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test



def carritoglobal(request):
	#var = {}

	data = {}
	print("#####################################sad###################")	

	if request.user.is_authenticated:
		print("#####################################sad###################")
	
		if request.user.has_perm('LogAuth.is_cliente'):


			if request.user.is_superuser == False:
				print("########################################################")
				var = {}
				var['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)
				OC = var['carrito'].orden.all()
				data = {
				        	'OC': OC,
				        	'carrito' : var
				        }
				return data

			else:
				return {}
		else:
			return {}
	else:
		return {}

			#ES TERRIBLMENTE IMPORTANTE DEVOLVER UN DICCIONARIO VACIO, SI NO, CRASHEA TODO EL SISTEMA
			##########################################################################################
