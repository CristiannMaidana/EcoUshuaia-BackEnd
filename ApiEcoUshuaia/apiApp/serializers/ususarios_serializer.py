from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apiApp.models import Usuarios


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
        read_only_field =  ('id_usuario',)
        validators = [
            UniqueTogetherValidator(
                queryset=Usuarios.objects.all(),
                fields=('email',),
                message= 'Este usuario ya existe en la base de datos'
            )
        ]
