from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from apiApp.models import Sensores
from apiApp.serializers.sensor_serializer import SensoresSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nombre_sensor', 'numero_serie')
    ordering_fields = ('id_sensor', 'nombre_sensor', 'fecha_instalacion_sensor', 'numero_serie')
    