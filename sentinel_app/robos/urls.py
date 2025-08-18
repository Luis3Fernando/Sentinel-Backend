from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UbigeoFromCoordsView, RiesgoViewSet, ModalidadesViewSet,
    HistorialViewSet, TemporalViewSet, ZonasViewSet
)

router = DefaultRouter()
router.register(r"riesgo", RiesgoViewSet, basename="riesgo")
router.register(r"modalidades", ModalidadesViewSet, basename="modalidades")
router.register(r"historial", HistorialViewSet, basename="historial")
router.register(r"temporal", TemporalViewSet, basename="temporal")
router.register(r"zonas", ZonasViewSet, basename="zonas")

urlpatterns = [
    path("ubigeo/", UbigeoFromCoordsView.as_view(), name="ubigeo-from-coords"),
    path("", include(router.urls)),
]