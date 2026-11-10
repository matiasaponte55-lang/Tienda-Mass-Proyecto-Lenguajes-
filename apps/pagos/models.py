# Módulo: Pagos y Facturación Electrónica (SUNAT)

from django.db import models
from apps.ventas.models import Pedido


# Modelo para registrar las transacciones de pago
class Pago(models.Model):
    METODOS = (
        ('yape', 'Yape (QR)'),
        ('plin', 'Plin (QR)'),
        ('tarjeta', 'Tarjeta Visa / Mastercard'),
        ('contraentrega', 'Contra Entrega en Efectivo'),
    )

    ESTADOS_PAGO = (
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    )

    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='pago')
    metodo = models.CharField(max_length=20, choices=METODOS, default='yape')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_operacion = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='pendiente')

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return f"Pago #{self.id} - {self.get_metodo_display()} (S/ {self.monto})"

    def confirmar_pago(self, codigo_operacion=None):
        if codigo_operacion:
            self.codigo_operacion = codigo_operacion
        self.estado = 'aprobado'
        self.save()
        self.pedido.actualizar_estado('pagado')


# Modelo para emisión de comprobante fiscal (Boleta o Factura con IGV 18%)
class Comprobante(models.Model):
    TIPOS = (
        ('boleta', 'Boleta de Venta Electrónica'),
        ('factura', 'Factura Electrónica'),
    )

    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='comprobante')
    tipo = models.CharField(max_length=10, choices=TIPOS, default='boleta')
    serie_numero = models.CharField(max_length=20, unique=True)
    documento_cliente = models.CharField(max_length=11)
    nombre_cliente = models.CharField(max_length=150)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comprobante Electrónico'
        verbose_name_plural = 'Comprobantes Electrónicos'

    def __str__(self):
        return f"{self.serie_numero} - {self.nombre_cliente} (S/ {self.total})"
