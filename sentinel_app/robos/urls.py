from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HistorialViewSet, ModalidadesViewSet, RiesgoViewSet, TemporalViewSet, ZonasViewSet

router = DefaultRouter()
router.register(r'historial', HistorialViewSet, basename='historial')
router.register(r'modalidades', ModalidadesViewSet, basename='modalidades')
router.register(r'riesgo', RiesgoViewSet, basename='riesgo')
router.register(r'temporal', TemporalViewSet, basename='temporal')
router.register(r'zonas', ZonasViewSet, basename='zonas')

urlpatterns = [
    path('', include(router.urls)),
]
