from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from LogAuth.models import Profile
from app1.models import Carrito
from LogAuth.forms import (
    UserForm,
    ProfileForm,
    UpdateUserForm
)
from django.db import IntegrityError


# Create your views here.
def login(request):
    template_name = 'login.html'
    data = {}

    auth.logout(request)

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )
        if user is not None:
            # flujo autenticado
            if user.is_active:
                # user valid
                auth.login(request, user)
                return redirect('fiesta:home')

            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Usuario o Contraseña incorrectos.'
                )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Usuario o Contraseña incorrectos.'
            )

            # user not valid

    return render(request, template_name, data)

def logout(request):
    auth.logout(request)
    return redirect('auth:login')

def register(request):
    data = {}

    data['form'] = UserForm(request.POST or None)

    if request.method == 'POST':
        if data['form'].is_valid():

            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    )

                profile = Profile.objects.create(
                    usuario=user,
                    fecha_nacimiento=request.POST['fecha_nacimiento'],
                    comuna=request.POST['comuna'],
                    direccion=request.POST['direccion'],
                    )
                carrito_nuevo = Carrito.objects.create(
                    profile=profile,
                    activo=True,
                    )

                permission = Permission.objects.get(codename='is_cliente')
                user.user_permissions.add(permission)

                user.save()
                profile.save()
                carrito_nuevo.save()

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Usuario creado con éxito.'
                    )
                return redirect('auth:login')
            except IntegrityError as ie:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Problemas al crear el usuario ERRO: {error}'.format(error=str(ie))
                    )
            except ValidationError as ve:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Problemas con la validación del formulario: {error}'.format(error=str(ve))
                    )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Problemas al crear el usuario'
                )

    template_name = 'register.html'
    return render(request, template_name, data)

def update_user(request, pk):
    template = 'update_user.html'
    data = {}

    data['profile_form'] = ProfileForm(request.POST or None, instance=request.user.profile)
    data['user_form'] = UpdateUserForm(request.POST or None, instance=request.user)

    if all([data['profile_form'].is_valid(), data['user_form'].is_valid()]):
        data['profile_form'].save()
        data['user_form'].save()

        return redirect('fiesta:home')     
    return render(request, template, data)