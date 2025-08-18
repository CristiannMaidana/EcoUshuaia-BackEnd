from rest_framework import viewsets, filters

from apiApp.models import Zonas
from apiApp.serializers.zonas_serializer import ZonasSerializer


class ZonasViewSet(viewsets.ModelViewSet):
    queryset = Zonas.objects.all()
    serializer_class = ZonasSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nombre_zona',)
    ordering_fields = ('id_zona', 'nombre_zona')