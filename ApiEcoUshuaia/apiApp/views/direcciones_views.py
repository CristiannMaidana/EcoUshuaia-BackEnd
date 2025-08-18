from rest_framework import viewsets, filters

from apiApp.models import Direcciones
from apiApp.serializers.direcciones_serializer import DireccionSerializer


class DireccionesViewSet(viewsets.ModelViewSet):
    queryset = Direcciones.objects.all()
    serializer_class = DireccionSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('calle',)
    ordering_fields = ('id_direccion', 'barrio', 'calle')