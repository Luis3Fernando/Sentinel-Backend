from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Historial, Modalidades, Riesgo, Temporal, Zonas
from .serializers import (
    HistorialSerializer,
    ModalidadesSerializer,
    RiesgoSerializer,
    TemporalSerializer,
    ZonasSerializer,
)
from .mixins import StandardResponseMixin
from datetime import datetime
from geopy.geocoders import Nominatim

class UbigeoFromCoordsView(StandardResponseMixin, APIView):
    def get(self, request, *args, **kwargs):
        lat = request.query_params.get("lat")
        lng = request.query_params.get("lng")
        if not lat or not lng:
            return Response(self.standard_response(
                data=[], messages=["Faltan parámetros lat o lng"], status_type="error"
            ))
        
        geolocator = Nominatim(user_agent="sentinel_app")
        location = geolocator.reverse(f"{lat}, {lng}")
        if location is None:
            return Response(self.standard_response(
                data=[], messages=["No se pudo obtener la ubicación"], status_type="error"
            ))

        address = location.raw.get("address", {})
        data = {
            "departamento": address.get("state"),
            "provincia": address.get("county"),
            "distrito": address.get("city"),
            "pais": address.get("country"),
            "lat": location.latitude,
            "lng": location.longitude
        }
        return Response(self.standard_response(data=[data], messages=["Ubicación obtenida"]))


class RiesgoViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = RiesgoSerializer
    queryset = Riesgo.objects.all()

    def list(self, request, *args, **kwargs):
        ubigeo = request.query_params.get("ubigeo")
        qs = self.queryset
        if ubigeo:
            qs = qs.filter(ubigeo_hecho=ubigeo)
        serializer = self.get_serializer(qs, many=True)
        return Response(self.standard_response(data=serializer.data))


class ModalidadesViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = ModalidadesSerializer
    queryset = Modalidades.objects.all()

    def list(self, request, *args, **kwargs):
        ubigeo = request.query_params.get("ubigeo")
        qs = self.queryset
        if ubigeo:
            qs = qs.filter(ubigeo_hecho=ubigeo)
        serializer = self.get_serializer(qs, many=True)
        return Response(self.standard_response(data=serializer.data))


class HistorialViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = HistorialSerializer
    queryset = Historial.objects.all()

    def list(self, request, *args, **kwargs):
        ubigeo = request.query_params.get("ubigeo")
        mes = request.query_params.get("mes")

        if not mes:
            mes = datetime.now().month
        else:
            mes = int(mes)

        qs = self.queryset
        if ubigeo:
            qs = qs.filter(ubigeo_hecho=ubigeo)
        if mes:
            qs = qs.filter(mes=mes)

        serializer = self.get_serializer(qs, many=True)
        return Response(self.standard_response(data=serializer.data))


class TemporalViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Temporal.objects.all()
    serializer_class = TemporalSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(self.standard_response(data=serializer.data))


class ZonasViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Zonas.objects.all()
    serializer_class = ZonasSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(self.standard_response(data=serializer.data))
