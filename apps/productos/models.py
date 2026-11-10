# Módulo: Catálogo e Inventario de Productos

from django.db import models
from datetime import date


# Modelo para registrar las categorías de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

    def total_productos(self):
        return self.productos.count()


# Modelo para registrar los productos y control de stock
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=5)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

    # Regla lógica: Verifica si el stock es crítico
    def tiene_stock_critico(self):
        return self.stock <= self.stock_minimo

    def descontar_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save(update_fields=['stock'])
            return True
        return False

    @property
    def es_stock_bajo(self):
        return self.stock <= self.stock_minimo

    # Regla lógica: Días restantes antes de vencer
    @property
    def dias_para_vencer(self):
        if self.fecha_vencimiento:
            return (self.fecha_vencimiento - date.today()).days
        return None

    # Regla lógica: Clasificación del estado de vencimiento
    @property
    def estado_vencimiento(self):
        dias = self.dias_para_vencer
        if dias is None:
            return 'Sin fecha'
        if dias < 0:
            return 'Vencido'
        if dias <= 15:
            return 'Próximo a vencer'
        return 'Vigente'
