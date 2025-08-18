from rest_framework import serializers

from apiApp.models import Zonas


class ZonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zonas
        fields = '__all__'
        read_only_fields = ('id_zona',)
        