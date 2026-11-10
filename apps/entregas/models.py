# Módulo: Logística, Despacho y Asignación de Repartidores

from django.db import models
from django.conf import settings
from apps.ventas.models import Pedido


# Modelo para la gestión y seguimiento logístico de entregas en Lima
class Entrega(models.Model):
    ZONAS_LIMA = (
        ('lima_centro', 'Lima Centro (Cercado, Breña, La Victoria)'),
        ('lima_norte', 'Lima Norte (Los Olivos, SMP, Comas)'),
        ('lima_sur', 'Lima Sur (Miraflores, Surco, Chorrillos)'),
        ('lima_este', 'Lima Este (SJL, Ate, Santa Anita)'),
    )

    ESTADOS_ENTREGA = (
        ('preparando', 'En Preparación'),
        ('en_camino', 'En Camino al Domicilio'),
        ('entregado', 'Entregado con Éxito'),
        ('fallido', 'Intento Fallido'),
    )

    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='entrega')
    repartidor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='entregas_asignadas'
    )
    zona = models.CharField(max_length=50, choices=ZONAS_LIMA, default='lima_centro')
    estado = models.CharField(max_length=20, choices=ESTADOS_ENTREGA, default='preparando')
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas y Envíos'

    def __str__(self):
        return f"Entrega Pedido #{self.pedido.numero_orden} - {self.get_estado_display()}"

    def iniciar_ruta(self):
        self.estado = 'en_camino'
        self.save(update_fields=['estado'])
        self.pedido.actualizar_estado('en_camino')

    def completar_entrega(self, nota=''):
        from django.utils import timezone
        self.estado = 'entregado'
        self.fecha_entrega = timezone.now()
        if nota:
            self.observaciones = f"{self.observaciones}\n{nota}".strip()
        self.save(update_fields=['estado', 'fecha_entrega', 'observaciones'])
        self.pedido.actualizar_estado('entregado')
