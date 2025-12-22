from rest_framework import viewsets, filters

from apiApp.models import CategoriaResiduos
from apiApp.serializers.categoria_residuos_serializer import CategoriaResiduosSerializer


class CategoriaResiduosViewSet(viewsets.ModelViewSet):
    queryset = CategoriaResiduos.objects.all()
    serializer_class = CategoriaResiduosSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('categoria',)
    ordering_fields = ('id_categoria_noticias',)
