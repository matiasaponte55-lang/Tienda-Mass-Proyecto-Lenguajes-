# Vistas para visualización de catálogo e inventario de productos

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import ProductoForm


def catalogo_view(request):
    productos = Producto.objects.filter(activo=True)
    categorias = Categoria.objects.all()
    return render(request, 'productos/catalogo.html', {
        'productos': productos,
        'categorias': categorias
    })


def detalle_producto_view(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})


def inventario_view(request):
    productos = Producto.objects.all()
    return render(request, 'productos/inventario.html', {'productos': productos})


def crear_producto_view(request):
    form = ProductoForm()
    return render(request, 'productos/form_producto.html', {'form': form, 'titulo': 'Nuevo Producto'})


def editar_producto_view(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(instance=producto)
    return render(request, 'productos/form_producto.html', {'form': form, 'producto': producto, 'titulo': 'Editar Producto'})


def toggle_producto_view(request, pk):
    return redirect('productos:inventario')
