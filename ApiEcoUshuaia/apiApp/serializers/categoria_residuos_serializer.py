from rest_framework import serializers

from apiApp.models import CategoriaResiduos


class CategoriaResiduosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaResiduos
        fields = '__all__'
