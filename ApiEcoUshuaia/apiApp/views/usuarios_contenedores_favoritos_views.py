from rest_framework import viewsets, filters
from apiApp.models import UsuariosContenedoresFavoritos
from apiApp.serializers.usuarios_contenedores_favoritos_serializer import UsuariosContenedoresFavoritosSerializer


class UsuarioContenedoresFavoritosViewsSet(viewsets.ModelViewSet):
    queryset = UsuariosContenedoresFavoritos.objects.all()
    serializer_class = UsuariosContenedoresFavoritosSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

