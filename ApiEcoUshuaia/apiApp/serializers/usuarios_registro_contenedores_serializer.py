from apiApp import serializers
from apiApp.models import UsuariosRegistroContenedores


class UsuariosRegistroContendoresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UsuariosRegistroContenedores
        read_only_fields = ('id_usuario_historial_residuos',)
