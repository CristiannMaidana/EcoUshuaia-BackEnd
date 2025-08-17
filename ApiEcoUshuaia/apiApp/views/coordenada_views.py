from rest_framework import viewsets, filters

from apiApp.models import Coordenadas
from apiApp.serializers.coordenada_serializer import CoordenadaSerializer


class CoordendaViewSet(viewsets.ModelViewSet):
    queryset = Coordenadas.objects.all()
    serializer_class = CoordenadaSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('tipo_archivo', 'tipo_coordenada')
    ordering_fields = ('id_coordenda', 'tipo_archivo', 'tipo_coordenada')