from rest_framework import viewsets, filters

from apiApp.models import CategoriaNoticias
from apiApp.serializers.categoria_noticias_serializer import CategoriaNoticiasSerializer


class CategoriaNoticiasViewSet(viewsets.ModelViewSet):
    queryset = CategoriaNoticias.objects.all()
    serializer_class = CategoriaNoticiasSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('categoria',)
    ordering_fields = ('id_categoria_noticias',)
