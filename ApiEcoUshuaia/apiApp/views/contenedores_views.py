from rest_framework import filters
from rest_framework import viewsets

from apiApp.models import Contenedores
from apiApp.serializers.contenedores_serializer import ContenedoresSerializer


class ContenedoresViewSet(viewsets.ModelViewSet):
    queryset = Contenedores.objects.select_related('id_zona', 'id_residuo',).all()
    serializer_class = ContenedoresSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nombre_contenedor', 'id_residuo__categoria')
    ordering_fields = ('nombre_contenedor', 'id_residuo__categoria','id_zona__nombre_zona')