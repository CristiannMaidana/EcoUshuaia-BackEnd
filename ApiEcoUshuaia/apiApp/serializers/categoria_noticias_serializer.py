from rest_framework import serializers

from apiApp.models import CategoriaNoticias


class CategoriaNoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNoticias
        fields = '__all__'
        read_only_fields = ('id_categoria_noticias')
