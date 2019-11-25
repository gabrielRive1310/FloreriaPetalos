from django.contrib import admin
from django.urls import path,include
from django.conf import settings #importar el archivo de configuracion
from django.conf.urls.static import static #importa el uso de ubicaciones estaticas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('flor.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
