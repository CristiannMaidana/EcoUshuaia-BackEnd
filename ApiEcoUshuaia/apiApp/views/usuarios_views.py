from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apiApp.models import Usuarios
from apiApp.serializers.usuarios_serializer import UsuariosSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.select_related('id_zona', 'id_tipo_usuario', 'user').all()
    serializer_class = UsuariosSerializer
    permission_classes = [AllowAny]

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id_usuario', 'email', )
    ordering_fields = ('id_usuario', 'nombre_usuario', 'apellido_usuario', 'id_zona__nombre_zona')

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated], url_path='me')
    def me(self, request):
        usuario = Usuarios.objects.select_related('id_zona', 'id_tipo_usuario').get(user=request.user)
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)
