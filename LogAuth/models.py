from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COMUNAS = (
	('RA', 'Rancagua'),
	('MA', 'Machali'),
)

class Profile(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	fecha_nacimiento = models.DateField(null=True, blank=True)
	comuna = models.CharField(choices=COMUNAS, max_length=2)
	direccion = models.CharField(max_length=80)

	class Meta:
		permissions = (
			('is_cliente', 'Es un cliente'),
			('is_admin', 'Es un admin'),
		)