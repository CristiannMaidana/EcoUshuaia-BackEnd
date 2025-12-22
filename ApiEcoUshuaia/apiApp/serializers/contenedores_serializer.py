from apiApp.models import Contenedores, Residuos
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ContenedoresSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Contenedores
        geo_field = 'coordenada'
        id_field = 'id_contenedor'
        fields = ('id_contenedor', 'nombre_contenedor', 'color_contenedor', 'capacidad_total', 'fecha_instalacion',
                  'ultimo_vaciado', 'descripcion_ubicacion', 'id_zona', 'id_residuo', 'id_mapa')
        read_only_field = ('id_contenedor',)

    def validate_capacidad_total(self, value):
        if value is not None and  value <= 0:
            raise serializers.ValidationError('La capacidad total debe ser mayor a 0.')
        return value
