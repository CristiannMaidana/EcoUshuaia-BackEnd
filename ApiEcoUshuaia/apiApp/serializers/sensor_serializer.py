from rest_framework import serializers

from apiApp.models import Contenedores, Sensores


class SensoresSerializer (serializers.ModelSerializer):
    id_contenedor = serializers.PrimaryKeyRelatedField (
        queryset = Contenedores.objects.only('id_contenedor'),
        allow_null = True,
        required = False,
    )

    class Meta:
        model = Sensores
        fields = '__all__'
        read_only_fields = ('id_sensor',)
        