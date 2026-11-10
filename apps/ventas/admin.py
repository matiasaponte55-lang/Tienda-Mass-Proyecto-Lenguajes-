# Administración de Pedidos y Ventas

from django.contrib import admin
from .models import Pedido, DetallePedido


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0
    readonly_fields = ('producto', 'cantidad', 'precio_unitario', 'subtotal')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero_orden', 'cliente', 'total', 'estado', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('numero_orden', 'cliente__username', 'cliente__dni')
    inlines = [DetallePedidoInline]
