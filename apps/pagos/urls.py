# Rutas del módulo de pagos y comprobantes

from django.urls import path
from . import views

app_name = 'pagos'

urlpatterns = [
    path('procesar/<int:pedido_id>/', views.procesar_pago_view, name='procesar'),
    path('comprobante/<int:comprobante_id>/', views.ver_comprobante_view, name='ver_comprobante'),
]
