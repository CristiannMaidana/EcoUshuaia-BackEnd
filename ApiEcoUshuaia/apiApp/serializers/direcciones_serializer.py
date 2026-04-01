from rest_framework import serializers
from django.contrib.gis.geos import Point

from apiApp.models import Direcciones


class CoordenadaField(serializers.Field):
    default_error_messages = {
        'invalid': 'La coordenada debe enviarse como un objeto.',
        'missing_latitud': 'La latitud es obligatoria dentro de coordenada.',
        'missing_longitud': 'La longitud es obligatoria dentro de coordenada.',
        'invalid_latitud': 'La latitud debe ser un número válido.',
        'invalid_longitud': 'La longitud debe ser un número válido.',
        'latitud_range': 'La latitud debe estar entre -90 y 90.',
        'longitud_range': 'La longitud debe estar entre -180 y 180.',
    }

    def to_representation(self, value):
        if value is None:
            return None

        return {
            'latitud': value.y,
            'longitud': value.x,
        }

    def to_internal_value(self, data):
        if data is None:
            return None

        if not isinstance(data, dict):
            self.fail('invalid')

        if 'latitud' not in data:
            self.fail('missing_latitud')

        if 'longitud' not in data:
            self.fail('missing_longitud')

        try:
            latitud = float(data['latitud'])
        except (TypeError, ValueError):
            self.fail('invalid_latitud')

        try:
            longitud = float(data['longitud'])
        except (TypeError, ValueError):
            self.fail('invalid_longitud')

        if not -90 <= latitud <= 90:
            self.fail('latitud_range')

        if not -180 <= longitud <= 180:
            self.fail('longitud_range')

        return Point(longitud, latitud, srid=4326)

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = '__all__'

    def _validate_required_text(self, value, field_name):
        if value is None or not str(value).strip():
            raise serializers.ValidationError(f'El campo {field_name} no puede estar vacío.')

        return str(value).strip()

    def _normalize_optional_text(self, value):
        if value is None:
            return None

        value = str(value).strip()
        return value or None

    def validate_calle(self, value):
        return self._validate_required_text(value, 'calle')

    def validate_ciudad(self, value):
        return self._validate_required_text(value, 'ciudad')

    def validate_provincia(self, value):
        return self._validate_required_text(value, 'provincia')

    def validate_pais(self, value):
        return self._validate_required_text(value, 'pais')

    def validate_numero(self, value):
        return self._normalize_optional_text(value)

    def validate_barrio(self, value):
        return self._normalize_optional_text(value)

    def validate_codigo_postal(self, value):
        return self._normalize_optional_text(value)
