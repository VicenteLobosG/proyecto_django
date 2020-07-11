from django import forms
from LogAuth.models import Profile
from django.contrib.auth.models import User

COMUNAS = (
	('RA', 'Rancagua'),
	('MA', 'Machali'),
)
class DateInput(forms.DateInput):
	input_type = 'date'

class UserForm(forms.Form):
	username = forms.CharField(label='Usuario', max_length=100)
	password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=100)
	fecha_nacimiento = forms.DateField(widget=DateInput, help_text='e.g. DD-MM-AAAA')
	comuna = forms.ChoiceField(label='Comuna', widget=forms.Select, choices=COMUNAS)
	direccion = forms.CharField(label='Direccion')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['fecha_nacimiento', 'comuna', 'direccion']
		widgets = {
			"fecha_nacimiento": forms.DateInput(attrs={
				'help_text':'e.g. DD-MM-AAAA'
				}),
			}

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username']