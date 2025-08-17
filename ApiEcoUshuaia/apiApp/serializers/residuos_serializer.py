from rest_framework import serializers
from apiApp.models import Residuos


class ResiduosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Residuos
        fields = '__all__'

    def validate_peso(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("El peso no puede ser negativo.")
        return value