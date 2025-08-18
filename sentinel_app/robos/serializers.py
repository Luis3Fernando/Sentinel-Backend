from rest_framework import serializers
from .models import Historial, Modalidades, Riesgo, Temporal, Zonas


class BaseResponseSerializer(serializers.Serializer):
    type = serializers.CharField()
    dto = serializers.ListField(child=serializers.DictField(), default=[])
    listMessage = serializers.ListField(child=serializers.CharField(), default=[])


class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = "__all__"


class ModalidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidades
        fields = "__all__"


class RiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riesgo
        fields = "__all__"


class TemporalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporal
        fields = "__all__"


class ZonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zonas
        fields = "__all__"
