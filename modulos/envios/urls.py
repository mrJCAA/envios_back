from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PaisView,
    DepartamentoView,
    #CargoView,
    #OficinaView,
    EnvioView,
    EnvioViewDetail,
    PersonaSegipView,
)

router = DefaultRouter()
#router.register('segip/<int:pk>/validar', PersonaSegipViewSet, base_name='segip_validar')
#router.register('nombre_ruta', OBJETOViewSet , base_name='nombre_ruta')

urlpatterns = [
    #path('api/', include(router.urls)),
    path('api/pais', PaisView.as_view(), name='pais'),
    path('api/departamento', DepartamentoView.as_view(), name='departamento'),
    #path('api/cargo', DepartamentoView.as_view(), name='cargo'),
    #path('api/oficina', DepartamentoView.as_view(), name='oficina'),
    path('api/envio', EnvioView.as_view(), name='envio'),
    path('api/envioDetalle/<int:pk>', EnvioViewDetail.as_view(), name='envio_detalle'),
    path('api/segip/<int:pk>/<slug:fecha>', PersonaSegipView.as_view(), name='segip_validar'),
]