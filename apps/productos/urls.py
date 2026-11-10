# Rutas del módulo de productos y catálogo

from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.catalogo_view, name='catalogo'),
    path('producto/<int:pk>/', views.detalle_producto_view, name='detalle'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('inventario/nuevo/', views.crear_producto_view, name='crear'),
    path('inventario/editar/<int:pk>/', views.editar_producto_view, name='editar'),
    path('inventario/toggle/<int:pk>/', views.toggle_producto_view, name='toggle'),
]
