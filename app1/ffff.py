data = {}
	template_name = 'masproducto.html'

	data['form'] = ProductoForm(request.POST, request.files)

	


	if data['form'].is_valid():
		data['form'].save()
		messages.add_message(
			request,
			messages.SUCCESS,
			'Producto ingresado!.')

		return redirect('fiesta:home')


	return render(request, template_name, data)







		nombre_p = forms.CharField(label='Nombre Producto', max_length=100)
		fecha_exp = forms.DateField(widget=DateInput, help_text='e.g. DD-MM-AAAA')
		precio = forms.IntegerField(label='Precio Producto')
		foto = forms.ImageField(label='Imagen')