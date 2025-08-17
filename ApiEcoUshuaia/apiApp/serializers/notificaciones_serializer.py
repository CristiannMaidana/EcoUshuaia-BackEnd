from datetime import date
from rest_framework import serializers

from apiApp.models import Notificaciones


class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'
        read_only_fields = ('id_notificacion',)

    def validate_fecha_envio(self, fecha_envio):
        today = date.today()
        if fecha_envio < today:
            raise serializers.ValidationError('La fecha no puede ser anterior a hoy.')
        return fecha_envio