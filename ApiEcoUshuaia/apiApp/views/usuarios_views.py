from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apiApp.models import Usuarios
from apiApp.serializers.usuarios_serializer import UsuariosSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.select_related('id_direccion', 'id_zona', 'id_tipo_usuario', 'user').all()
    serializer_class = UsuariosSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id_usuario', 'email', )
    ordering_fields = ('id_usuario', 'nombre_usuario', 'apellido_usuario', 'id_zona__nombre_zona')

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset

        return queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get', 'patch'], permission_classes=[IsAuthenticated], url_path='me')
    def me(self, request):
        usuario = self.get_queryset().select_related('id_direccion', 'id_zona', 'id_tipo_usuario').get(user=request.user)

        if request.method == 'GET':
            serializer = self.get_serializer(usuario)
            return Response(serializer.data)

        serializer = self.get_serializer(usuario, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
