from rest_framework import viewsets, filters

from apiApp.models import UsuariosHistorialesResiduos
from apiApp.serializers.usuarios_historiales_residuos_serializer import UsuariosHistorialesResiduosSerializer


class UsuariosHistorialesResiduosViewSet(viewsets.ModelViewSet):
    queryset = UsuariosHistorialesResiduos.objects.select_related('id_residuo', 'id_usuario',).all()
    serializer_class = UsuariosHistorialesResiduosSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id_residuo',)
    ordering_fields = ('unidad', 'id_usuario', 'id_residuo__nombre')