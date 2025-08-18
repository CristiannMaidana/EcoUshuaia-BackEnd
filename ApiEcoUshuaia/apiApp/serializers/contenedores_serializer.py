from apiApp.models import Contenedores
from rest_framework import serializers


class ContenedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenedores
        fields = '__all__'
        read_only_field = ('id_contenedor',)
        