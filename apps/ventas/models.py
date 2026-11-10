# Módulo: Ventas, Carrito de Compras y Pedidos

from django.db import models
from django.conf import settings
from apps.productos.models import Producto


# Modelo que registra cada orden de compra realizada por un cliente
class Pedido(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('en_camino', 'En Camino'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    numero_orden = models.CharField(max_length=20, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    igv = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    direccion_entrega = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha']

    def __str__(self):
        return f"Pedido #{self.numero_orden} - {self.cliente.username}"

    def calcular_totales(self):
        from decimal import Decimal
        sub = sum((d.subtotal for d in self.detalles.all()), Decimal('0.00'))
        self.subtotal = sub
        self.igv = (sub * Decimal('0.18')).quantize(Decimal('0.01'))
        self.total = self.subtotal + self.igv
        self.save(update_fields=['subtotal', 'igv', 'total'])

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.save(update_fields=['estado'])


# Detalle de cada producto incluido dentro de una orden de pedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedidos'

    def save(self, *args, **kwargs):
        if not self.subtotal and self.precio_unitario and self.cantidad:
            self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"
