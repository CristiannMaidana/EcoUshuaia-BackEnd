from rest_framework import serializers

from apiApp.models import UsuariosContenedoresFavoritos


class UsuariosContenedoresFavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosContenedoresFavoritos
        fields = '__all__'