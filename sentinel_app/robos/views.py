from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Historial, Modalidades, Riesgo, Temporal, Zonas
from .serializers import HistorialSerializer, ModalidadesSerializer, RiesgoSerializer, TemporalSerializer, ZonasSerializer
from .mixins import StandardResponseMixin
from datetime import datetime

class UbigeoFromCoordsView(StandardResponseMixin, APIView):
    """
    Recibe lat/lng y devuelve UBIGEO
    """
    def get(self, request, *args, **kwargs):
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        listMessage = []

        if not lat or not lng:
            listMessage.append("Faltan parámetros lat o lng")
            return Response(self.standard_response(data=[], messages=listMessage, status_type='error'))

        # TODO: aquí usarías la lógica para convertir coordenadas a UBIGEO
        # Por ahora devolvemos un ejemplo fijo:
        ubigeo = 150101  # ejemplo
        return Response(self.standard_response(data=[{"ubigeo": ubigeo}], messages=["UBIGEO obtenido"]))
    
class RiesgoViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = RiesgoSerializer
    queryset = Riesgo.objects.all()

    def list(self, request, *args, **kwargs):
        ubigeo = request.query_params.get('ubigeo')
        qs = self.queryset
        if ubigeo:
            qs = qs.filter(ubigeo_hecho=ubigeo)
        serializer = self.get_serializer(qs, many=True)
        return Response(self.standard_response(data=serializer.data))


class ModalidadesViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = ModalidadesSerializer
    queryset = Modalidades.objects.all()

    def list(self, request, *args, **kwargs):
        ubigeo = request.query_params.get('ubigeo')
        qs = self.queryset
        if ubigeo:
            qs = qs.filter(ubigeo_hecho=ubigeo)
        serializer = self.get_serializer(qs, many=True)
        return Response(self.standard_response(data=serializer.data))


class HistorialViewSet(StandardResponseMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = HistorialSerializer
    queryset = Historial.objects.all()

    def list(self, request, *args, **kwargs):
        ubigeo = request.query_params.get('ubigeo')
        mes = request.query_params.get('mes')

        # Si no se pasa mes, usamos el mes actual
        if not mes:
            mes = datetime.now().month
        else:
            mes = int(mes)  # convertimos a entero por si viene como string

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