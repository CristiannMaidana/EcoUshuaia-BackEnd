from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from apiApp.models import Contenedores
from apiApp.serializers.contenedores_serializer import ContenedoresSerializer


class ContenedoresViewSet(viewsets.ModelViewSet):
    queryset = Contenedores.objects.select_related('id_zona', 'id_residuo', 'id_coordenada', 'id_mapa',).all()
    serializer_class = ContenedoresSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ('nombre_contenedor', 'id_residuo__nombre')
    ordering_fields = ('nombre_contenedor', 'id_residuo__categoria','id_zona__nombre_zona')
    filter_fields = {
        'id_residuo': ['exact'],
        'id_residuo__nombre': ['exact'],
        'id_residuo__categoria': ['exact'],
    }