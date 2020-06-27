from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
import datetime


@login_required
def home(request):
	template_name = 'home.html'
	data = {}

	data['title'] = 'Home'

	#question_list = Question.objects.all()
	data['query']=''
	#caso de busqueda
	if 'q' in request.GET:
		#se obtiene la q de donde esta parado

		data['query']=request.GET.get('q')
		lista_productos = Producto.objects.filter(nombre_p__icontains=data['query'])

	#caso normal
	"""
	else:
		#question_list = Question.objects.all()

	paginator=Paginator(question_list, 4)
	#la pagina viene aqui con los datos
	page=request.GET.get('page',1)

	try:
		data['questions']=paginator.page(page)
		print(data['questions'])
	except PageNotAnInteger:
		data['questions']=paginator.page(1)
	except EmptyPage:
		data['questions']=paginator.page(page.num_pages)
	"""
	return render(request, template_name, data)


@login_required
def articulos(request):
	template_name = 'articulos.html'
	data = {}
	data['title'] = 'Articulos'
	data['productos'] = Producto.objects.all()


	return render(request, template_name, data)


"""
class Carrito(models.Model):
	orden = models.ManyToManyField(OrdenCompra, null=True, blank=True) ---
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE) --- lo tengo
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True, blank=True) --- crear
	activo = models.BooleanField(default=True) --- lo tengo

"""

@login_required
def addproducto(request, producto_id):
	template_name = 'home.html' #cambiar esta wea
	#venta = Venta.objects.create(hora_venta=datetime.now(),) cuando el usuario apreta 
	#procesar la compra, ahi deberia guardar este dato con el total de la venta
	data = {}
	data['productos'] = Producto.objects.all()

	for producto in data['productos']:
		if producto.id == producto_id:
			#la cantidad
			
			data['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)
			


			if data['carrito'].orden.all().exists():
				for x in data['carrito'].orden.all():
					if x.producto.id == producto_id:
						OrdenCompra.objects.get(id=x.producto.id).update(cantidad_producto=cantidad_producto+1)
					else:
						print("#################1")
						orden_compra = OrdenCompra.objects.create(producto=producto)
						data['carrito'].orden.add(orden_compra)
			else:
				print("#################3")
				orden_compra = OrdenCompra.objects.create(producto=producto)
				data['carrito'].orden.add(orden_compra)



	return render(request, template_name)


@login_required
def carrito(request):
	template_name = 'carrito.html'
	data = {}
	data['title'] = 'Carrito'
	data['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)
	data['total'] = 0

	for  producto in data['carrito'].orden.all():
		data['total'] += producto.producto.precio*producto.cantidad_producto

	if not data['carrito'].orden.all():
		template_name = 'carrito_vacio.html'
	else:
		template_name = 'carrito.html'

	return render(request, template_name, data)


@login_required
def comprar(request, pk):

	data = {}
	data['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True, pk=pk)
	data['inventario'] = Inventario.objects.all()
	total = 0

	###Restar inventario

	for  producto in data['carrito'].orden.all():
		for inventario in data['inventario']:
			if inventario.producto.nombre_p == producto.producto.nombre_p:
				Inventario.objects.filter(producto=producto.producto).update(cantidad=inventario.cantidad-producto.cantidad_producto)

	###Creando la venta

	for  producto in data['carrito'].orden.all():
		total += producto.producto.precio*producto.cantidad_producto

	venta_nueva = Venta.objects.create(
		hora_venta=datetime.datetime.now(),
		total=total,
		)

	venta_nueva.save()

	###Seteando el carrito actual a no activo y asignando la venta

	Carrito.objects.filter(profile__exact=request.user.profile, activo=True).update(activo=False, venta=venta_nueva)

	###Creando nuevo carrito

	carrito_nuevo = Carrito.objects.create(
		profile=request.user.profile,
		activo=True,
		)

	carrito_nuevo.save()

	return redirect('fiesta:home')