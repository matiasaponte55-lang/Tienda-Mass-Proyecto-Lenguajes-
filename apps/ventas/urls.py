# Rutas del módulo de ventas, pedidos y reportes

from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('carrito/', views.ver_carrito_view, name='carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_carrito_view, name='agregar_carrito'),
    path('carrito/restar/<int:producto_id>/', views.restar_carrito_view, name='restar_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_carrito_view, name='eliminar_carrito'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('mis-pedidos/', views.mis_pedidos_view, name='mis_pedidos'),
    path('pedido/<int:pedido_id>/', views.detalle_pedido_view, name='detalle_pedido'),
    path('reportes/', views.reportes_ventas_view, name='reportes'),
]
