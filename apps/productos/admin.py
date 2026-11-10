# Módulo: Administración de Catálogo y Productos

from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'codigo',
        'categoria',
        'precio',
        'stock',
        'stock_minimo',
        'mostrar_estado_stock',
        'activo'
    )
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'codigo')

    # Regla visual para alertar si el stock está por debajo del mínimo
    @admin.display(description='Estado del inventario')
    def mostrar_estado_stock(self, obj):
        if obj.stock <= obj.stock_minimo:
            return 'STOCK BAJO'
        return 'STOCK NORMAL'
