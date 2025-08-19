from rest_framework import viewsets, filters

from apiApp.models import UsuariosRegistroContenedores
from apiApp.serializers.usuarios_registro_contenedores_serializer import UsuariosRegistroContendoresSerializer


class UsuarioRegistroContenedoresView(viewsets.ModelViewSet):
    queryset = UsuariosRegistroContenedores.objects.select_related('id_usuario', 'id_contenedor',).all()
    serializer_class = UsuariosRegistroContendoresSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id_usuario__email', )
    ordering_fields = ('id_usuario_registro_contenedor', 'id_usuario__email', 'id_contenedor__id_residuo__nombre')