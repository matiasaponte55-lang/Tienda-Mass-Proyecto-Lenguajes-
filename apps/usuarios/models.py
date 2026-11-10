# Módulo: Autenticación y Usuarios con roles

from django.db import models
from django.contrib.auth.models import AbstractUser


# Modelo personalizado de usuario para manejar roles y datos peruanos
class Usuario(AbstractUser):
    ROLES = (
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
        ('repartidor', 'Repartidor'),
    )

    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')
    dni = models.CharField(max_length=8, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

    def es_administrador(self):
        return self.rol == 'admin' or self.is_superuser

    def es_repartidor(self):
        return self.rol == 'repartidor'
