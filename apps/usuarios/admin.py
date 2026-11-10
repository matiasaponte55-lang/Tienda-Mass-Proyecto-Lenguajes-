# Módulo: Administración de Usuarios

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


# Registro de usuario personalizado en el panel admin
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'dni', 'is_staff')
    list_filter = ('rol', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Datos Adicionales', {'fields': ('rol', 'dni', 'telefono', 'direccion')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos Adicionales', {'fields': ('rol', 'dni', 'telefono', 'direccion')}),
    )
