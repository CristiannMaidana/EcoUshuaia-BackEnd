from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from apiApp.models import Residuos
from apiApp.serializers.residuos_serializer import ResiduosSerializer


class ResiduosViewSet(ModelViewSet):
    queryset = (Residuos.objects.all().order_by('id_residuo'))
    serializer_class = ResiduosSerializer
    serializer_class = ResiduosSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id_residuo', 'categoria', 'nombre']
    ordering_fields = ['id_residuo', 'nombre', 'peso', 'categoria']
