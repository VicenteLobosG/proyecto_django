from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
import datetime
from app1.forms import ProductoForm



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
	template_name = 'articulos.html' #cambiar esta wea
	#venta = Venta.objects.create(hora_venta=datetime.now(),) cuando el usuario apreta 
	#procesar la compra, ahi deberia guardar este dato con el total de la venta
	data = {}
	data['productos'] = Producto.objects.all()

			
	data['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)



	#OC tiene todas las ordenes con el producto seleccionado
	OC = data['carrito'].orden.all().filter(producto__id=producto_id).exists()
	print(OC)

	varlo = data['carrito'].orden.all().exists()


	print(varlo)

	if varlo == True: #Si existen ordenes de compra para el carrito

		if OC == True: #Si existen ordenes que tengan productos con esa ID
			

			var = data['carrito'].orden.get(producto__id=producto_id)
			print(var)
			var.cantidad_producto = var.cantidad_producto+1


			product = Producto.objects.get(id=producto_id)
			var.total = product.precio * var.cantidad_producto

			var.save()
			print("###################7")

		else: #Si no existen ordenes que tengan productos con esa ID
			P_ins = Producto.objects.get(id=producto_id)
								
			orden_compra = OrdenCompra.objects.create(producto=P_ins)
			OrdenCompra.objects.filter(id=orden_compra.id).update(total=P_ins.precio)
			data['carrito'].orden.add(orden_compra)
			print("#################5")

	else:
		P_ins = Producto.objects.get(id=producto_id)
								
		orden_compra = OrdenCompra.objects.create(producto=P_ins)
		OrdenCompra.objects.filter(id=orden_compra.id).update(total=P_ins.precio)
		print(orden_compra.id)
		data['carrito'].orden.add(orden_compra)
		print("#################1")



	data['carrotemp'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)
	return render(request, template_name, data)


@login_required
def quitarproducto(request, producto_id):

	data = {}
	

	data['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)

	varlo = data['carrito'].orden.all().exists() #todas las ordenes de compra del carrito

	#OC tiene todas las ordenes con el producto seleccionado
	OC = data['carrito'].orden.all().filter(producto__id=producto_id).exists()

	if varlo == True:
		if OC == True:

			var = data['carrito'].orden.get(producto__id=producto_id)
			
			if var.cantidad_producto == 1:
				OrdenCompra.objects.filter(producto__id=producto_id).delete()
				print("##################HOLA")

			if var.cantidad_producto > 1:
				
				var.cantidad_producto = var.cantidad_producto - 1
				product = Producto.objects.get(id=producto_id)
				var.total = product.precio * var.cantidad_producto
				var.save()

		else:
			messages.add_message(
                request,
                messages.ERROR,
                'No puede quitar este producto!.'
                )
	else:
		messages.add_message(
            request,
            messages.ERROR,
            'No puede quitar este producto!.'
            )


	return redirect('fiesta:articulos')


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



@login_required
def vaciar(request):
	
	data = {}
	
	data['carrito'] = Carrito.objects.get(profile__exact=request.user.profile, activo=True)
	data['carrito'].orden.all().delete()
	print(data['carrito'].orden)

	return redirect('fiesta:home')


@login_required
def compras(request):
	template_name = 'compras.html'
	data = {}

	data['carritos'] = Carrito.objects.all().filter(profile__exact=request.user.profile)
	exc = Carrito.objects.get(profile__exact=request.user.profile, venta=None)
	



	for x in data['carritos']:
		print("----------------")
		print(x)
		print(exc)
		if x == exc:
			pass
		else:
			data['carrito_final'] = x
			

		data['var_orden'] = x.orden.all()
		data['venta_venta'] = x.venta


		for i in data['var_orden']:
			print(i.producto.fecha_exp)

	
		
	return render(request, template_name, data)
	#ventas = Venta.objects.all().filter(carrito=request.user.profile.carrito.id)


@permission_required('app1.add_producto')
def masproducto(request):
	data = {}
	template_name = 'masproducto.html'

	if request.method == "POST":
		data['form'] = ProductoForm(request.POST, request.FILES)

		


		if data['form'].is_valid():
			data['form'].save()
			messages.add_message(
				request,
				messages.SUCCESS,
				'Producto ingresado!.')

			return redirect('fiesta:home')

	else:
		data['form'] = ProductoForm(request.POST or None)


	return render(request, template_name, data)



@permission_required('app1.change_producto')
def update(request, pk):
    template_name = 'update.html'
    data = {}

    producto = Producto.objects.get(pk=pk)
    data['form'] = ProductoForm(instance=producto, data=request.POST)

    if data['form'].is_valid():
        data['form'].save()
        return redirect('fiesta:home')

    return render(request, template_name, data)

@permission_required('app1.delete_producto')
def delete(request, pk):
    data = {}
    data['producto'] = Producto.objects.get(pk=pk)

    if request.method == 'POST':
        data['producto'].delete()
        return redirect('fiesta:home')

    template_name = 'delete.html'


    return render(request, template_name, data)

def read_compras(request):
	data = {}

	data['carritos'] = Carrito.objects.all()

	template_name = 'read_compras.html'

	return render(request, template_name, data)