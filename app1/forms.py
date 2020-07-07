from django import forms
from app1.models import Producto


class ProductoForm(forms.ModelForm):
	class Meta:

		model = Producto
		fields = (
			'nombre_p',
			'fecha_exp',
			'precio',
			'foto',
		)




