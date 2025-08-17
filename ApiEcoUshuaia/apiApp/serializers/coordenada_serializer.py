from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apiApp.models import Coordenadas


class CoordenadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenadas
        fields = '__all__'
        read_only_fields = ('id_coordenada',)
        validators = [
            UniqueTogetherValidator(
                queryset=Coordenadas.objects.all(),
                fields=('coordenada',),
                message='Este coordenada ya existe',
            )
        ]