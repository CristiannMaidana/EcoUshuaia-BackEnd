from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from apiApp.models import MedicionSensores
from apiApp.serializers.medicion_sensor_serializer import MedicionSensorSerializar


class MedicionSensoresViewSet(ModelViewSet):
    queryset = MedicionSensores.objects.all()
    serializer_class = MedicionSensorSerializar

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id_contenedor', 'id_sensor', 'fecha_hora_medicion')
    ordering_fields = ('fehca_hora_medicion', 'id_medicion_sensor')
