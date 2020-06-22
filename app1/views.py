from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
=======
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
	return render(request, template_name, data)


@login_required
def carrito(request):
	template_name = 'carrito.html'
	data = {}
	data['title'] = 'Carrito'
	return render(request, template_name, data)
>>>>>>> acb27ce7fa1f8b24c3ec6d86fdd2cab1240352f8
