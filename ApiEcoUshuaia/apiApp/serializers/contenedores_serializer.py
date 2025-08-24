from apiApp.models import Contenedores
from rest_framework import serializers


class ContenedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenedores
        fields = '__all__'
        read_only_field = ('id_contenedor',)

    def validate_capacidad_total(self, value):
        if value is not None and  value <= 0:
            raise serializers.ValidationError('La capacidad total debe ser mayor a 0.')
        return value
