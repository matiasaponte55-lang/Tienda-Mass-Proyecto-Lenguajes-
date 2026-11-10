# Vistas para visualización de pantallas de entregas y seguimiento

from django.shortcuts import render, redirect, get_object_or_404
from apps.ventas.models import Pedido
from .models import Entrega


def seguimiento_view(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'entregas/seguimiento.html', {'pedido': pedido})


def panel_repartidor_view(request):
    return render(request, 'entregas/panel_repartidor.html')


def actualizar_estado_view(request, entrega_id):
    return redirect('entregas:panel_repartidor')


def admin_entregas_view(request):
    return render(request, 'entregas/admin_entregas.html')
