from apiApp.models import Contenedores, Residuos
from rest_framework import serializers


class ResiduoLiteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_residuo')
    class Meta:
        model = Residuos
        fields = ('id', 'nombre','categoria')


class ContenedoresSerializer(serializers.ModelSerializer):
    id_residuo = serializers.PrimaryKeyRelatedField(
        queryset=Residuos.objects.all(),
        write_only=True
    )

    residuo = ResiduoLiteSerializer(source='id_residuo', read_only=True)

    class Meta:
        model = Contenedores
        fields = ('id_contenedor', 'nombre_contenedor', 'color_contenedor', 'capacidad_total', 'fecha_instalacion',
                  'ultimo_vaciado', 'descripcion_ubicacion', 'id_zona', 'id_residuo', 'id_coordenada', 'id_mapa',
                  'residuo')
        read_only_field = ('id_contenedor',)

    def validate_capacidad_total(self, value):
        if value is not None and  value <= 0:
            raise serializers.ValidationError('La capacidad total debe ser mayor a 0.')
        return value
