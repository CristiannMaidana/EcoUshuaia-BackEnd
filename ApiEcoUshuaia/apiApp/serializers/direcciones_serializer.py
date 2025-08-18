from rest_framework import serializers

from apiApp.models import Direcciones


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = '__all__'
        read_only_fields = ('id_direccion',)