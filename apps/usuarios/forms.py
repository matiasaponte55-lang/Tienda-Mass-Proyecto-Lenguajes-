# Formularios de autenticación y validación de usuarios

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


# Formulario de registro para clientes con validación de DNI peruano
class RegistroClienteForm(UserCreationForm):
    dni = forms.CharField(max_length=8, min_length=8, required=True, label="DNI (8 dígitos)")
    telefono = forms.CharField(max_length=15, required=False, label="Teléfono / Celular")
    direccion = forms.CharField(max_length=255, required=False, label="Dirección de entrega")

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'dni', 'telefono', 'direccion')

    # Regla lógica de validación: DNI solo números y 8 dígitos
    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if not dni.isdigit():
            raise forms.ValidationError("El DNI debe contener solo números.")
        if Usuario.objects.filter(dni=dni).exists():
            raise forms.ValidationError("Este DNI ya se encuentra registrado.")
        return dni

    def save(self, commit=True):
        user = super().save(commit=False)
        user.rol = 'cliente'
        if commit:
            user.save()
        return user
