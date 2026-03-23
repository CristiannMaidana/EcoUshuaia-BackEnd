from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apiApp.serializers.autentificacion_usuario_serializer import AutentificacionUsuarioSerializer
from apiApp.serializers.usuarios_serializer import UsuariosSerializer


class AutentificacionUsuarioViewSet(viewsets.GenericViewSet):
    serializer_class = AutentificacionUsuarioSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        perfil = serializer.validated_data["perfil"]

        data = UsuariosSerializer(perfil).data
        return Response(data, status=200)
