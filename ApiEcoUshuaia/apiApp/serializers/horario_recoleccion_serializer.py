from rest_framework import serializers

from apiApp.models import HorariosRecoleccion


class HorarioRecoleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorariosRecoleccion
        fields = '__all__'
        read_only_fields = ('id_horario_recoleccion',)
