from decimal import Decimal

from django.utils import timezone
from rest_framework import serializers

from apiApp.models import Sensores, Contenedores, MedicionSensores, UmbralLlenado


class MedicionSensorSerializar(serializers.ModelSerializer):
    sensor_id = serializers.PrimaryKeyRelatedField(
        queryset = Sensores.objects.all(),
        source = 'id_sensor'
    )

    contenedor_id = serializers.PrimaryKeyRelatedField(
        queryset = Contenedores.objects.all(),
        source= 'id_contenedor'
    )

    fecha_hora_medcion = serializers.DateTimeField(
        required = False,
        default = serializers.CreateOnlyDefault(timezone.now)
    )

    volumen_medido = serializers.DecimalField(
        max_digits=8, decimal_places=2,
        required=True, allow_null=False,
        min_value=0
    )

    alerta_generada = serializers.BooleanField(read_only=True)

    class Meta:
        model = MedicionSensores
        fields = (
            'id_medicion_sensor',
            'fecha_hora_medicion',
            'volumen_medido',
            'alerta_generada',
            'sensor_id',
            'contenedor_id'
        )
        read_only_fields = ('id_medicion_sensor',)

    def validate(self, attrs):
        volumen = attrs['volumen_medido']

        umbral = UmbralLlenado.objects.order_by('-pk').first()
        if umbral is None:
            raise serializers.ValidationError(
                {'umbral': 'No hay umbral_llenado configurado.'}
            )

        limite = umbral.alto_max
        if limite is None:
            raise serializers.ValidationError(
                {'umbral': 'El umbral (alto_max) está en Null.'}
            )

        limite_dec = Decimal(str(limite))
        attrs['alerta_generada']= (volumen >= limite_dec)
        
        return attrs

