from django.utils import timezone
from rest_framework import serializers
from apiApp.models import Notificaciones


class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'
        read_only_fields = ('id_notificacion',)

    def validate_fecha_envio(self, value):
        if timezone.is_naive(value):
            value = timezone.make_aware(value, timezone.get_current_timezone())

        fecha_value = timezone.localtime(value).date()
        today = timezone.localdate()

        if fecha_value < today:
            raise serializers.ValidationError('La fecha no puede ser anterior a hoy.')
        return value
