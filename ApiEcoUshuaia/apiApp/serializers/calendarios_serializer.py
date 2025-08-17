from django.utils import timezone

from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from apiApp.models import Calendarios


class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendarios
        fields = '__all__'
        read_only_fields = ('id_calendario',)
        validators = [
            UniqueTogetherValidator(
                queryset=Calendarios.objects.all(),
                fields=('hora', 'fecha'),
                message='Ya hay un calendario con ese horario.'
            )
        ]

    def validate_fecha(self, value):
        today = timezone.localdate()
        if value < today:
            raise serializers.ValidationError('La fecha no puede ser anterior a hoy.')
        return value