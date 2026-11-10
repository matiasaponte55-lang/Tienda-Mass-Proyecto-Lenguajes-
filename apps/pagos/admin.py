# Módulo: Administración de Pagos y Comprobantes

from django.contrib import admin
from .models import Pago, Comprobante


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'metodo', 'monto', 'estado', 'fecha')
    list_filter = ('metodo', 'estado')


@admin.register(Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('serie_numero', 'tipo', 'nombre_cliente', 'total', 'fecha_emision')
    list_filter = ('tipo', 'fecha_emision')
    search_fields = ('serie_numero', 'documento_cliente', 'nombre_cliente')
