# Vistas para visualización de interfaces de autenticación y perfil

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroClienteForm


def inicio_view(request):
    return redirect('usuarios:login')


def login_view(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('usuarios:login')


def registro_view(request):
    form = RegistroClienteForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def perfil_view(request):
    return render(request, 'usuarios/perfil.html')


def panel_admin_view(request):
    return render(request, 'usuarios/panel_admin.html')
