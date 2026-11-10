# Módulo: Administración de Logística y Entregas

from django.contrib import admin
from .models import Entrega


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'repartidor', 'zona', 'estado', 'fecha_asignacion')
    list_filter = ('zona', 'estado', 'fecha_asignacion')
    search_fields = ('pedido__numero_orden', 'repartidor__username')
