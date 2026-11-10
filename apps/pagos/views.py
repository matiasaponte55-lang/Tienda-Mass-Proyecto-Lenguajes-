# Vistas para visualización de pantallas de pago y comprobante

from django.shortcuts import render, redirect, get_object_or_404
from apps.ventas.models import Pedido
from .models import Pago, Comprobante


def procesar_pago_view(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pagos/procesar.html', {'pedido': pedido})


def ver_comprobante_view(request, comprobante_id):
    comprobante = get_object_or_404(Comprobante, id=comprobante_id)
    return render(request, 'pagos/comprobante.html', {'comprobante': comprobante})
