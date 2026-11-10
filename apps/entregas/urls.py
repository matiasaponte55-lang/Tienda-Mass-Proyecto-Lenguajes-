# Rutas del módulo de logística, despacho y entregas

from django.urls import path
from . import views

app_name = 'entregas'

urlpatterns = [
    path('seguimiento/<int:pedido_id>/', views.seguimiento_view, name='seguimiento'),
    path('panel-repartidor/', views.panel_repartidor_view, name='panel_repartidor'),
    path('actualizar/<int:entrega_id>/', views.actualizar_estado_view, name='actualizar_estado'),
    path('administrar/', views.admin_entregas_view, name='admin_entregas'),
]
