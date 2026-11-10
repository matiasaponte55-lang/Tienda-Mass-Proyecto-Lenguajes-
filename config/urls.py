"""
URL configuration for Tienda Mass project.
Enrutador principal del proyecto que conecta todas las apps del negocio.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.usuarios.views import inicio_view

urlpatterns = [
    # Ruta raíz: inicia obligatoriamente en login si no hay sesión activa
    path('', inicio_view, name='inicio'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.usuarios.urls')),
    path('catalogo/', include('apps.productos.urls')),
    path('ventas/', include('apps.ventas.urls')),
    path('pagos/', include('apps.pagos.urls')),
    path('entregas/', include('apps.entregas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
