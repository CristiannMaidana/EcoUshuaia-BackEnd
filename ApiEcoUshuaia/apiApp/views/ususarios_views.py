from rest_framework import viewsets, filters

from apiApp.models import Usuarios
from apiApp.serializers.ususarios_serializer import UsuariosSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.select_related('id_zona', 'id_tipo_usuario').all()
    serializer_class = UsuariosSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id_usuario', 'email', )#'id_zona__nombre_zona', 'id_tipo_ususario__tipo_usuario')#
    ordering_fields = ('id_usuario', 'nombre_usuario', 'apellido_usuario', 'id_zona__nombre_zona')
