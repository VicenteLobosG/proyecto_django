from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from LogAuth.models import Profile
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
                return redirect('Venta')

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
    return redirect('login')