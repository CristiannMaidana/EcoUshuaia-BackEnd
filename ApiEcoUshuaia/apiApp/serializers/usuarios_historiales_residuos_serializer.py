from rest_framework import serializers

from apiApp.models import UsuariosHistorialesResiduos


class UsuariosHistorialesResiduosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosHistorialesResiduos
        fields = '__all__'
        read_only_fields = ('id_usuario_historial_residuos',)