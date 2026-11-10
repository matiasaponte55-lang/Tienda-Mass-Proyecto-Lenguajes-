# Vistas para visualización de interfaces de compra y pedidos

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from apps.productos.models import Producto


def ver_carrito_view(request):
    return render(request, 'ventas/carrito.html')


def agregar_carrito_view(request, producto_id):
    return redirect('ventas:carrito')


def restar_carrito_view(request, producto_id):
    return redirect('ventas:carrito')


def eliminar_carrito_view(request, producto_id):
    return redirect('ventas:carrito')


def checkout_view(request):
    return render(request, 'ventas/checkout.html')


def mis_pedidos_view(request):
    pedidos = Pedido.objects.all()
    return render(request, 'ventas/mis_pedidos.html', {'pedidos': pedidos})


def detalle_pedido_view(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'ventas/detalle_pedido.html', {'pedido': pedido})


def reportes_ventas_view(request):
    return render(request, 'ventas/reportes.html')
