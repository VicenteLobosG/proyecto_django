from django import forms
from app1.models import Producto, Inventario
import datetime

class ProductoForm(forms.ModelForm):
	class Meta:

		model = Producto
		fields = (
			'nombre_p',
			'fecha_exp',
			'precio',
			'foto',
		)




class InventarioForm(forms.ModelForm):
	class Meta:

		hora_act = datetime.datetime.now()

		model = Inventario
		fields = (
			'cantidad',
		)


