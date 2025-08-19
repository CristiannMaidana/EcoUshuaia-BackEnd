import re

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

    def validate_nombre_usuario(self, nombre):
        if not nombre or not nombre.strip():
            raise serializers.ValidationError('El nombre no puede estar vacío.')

        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre):
            raise serializers.ValidationError(
                'El nombre solo puede contener letras y espacios, sin números ni caracteres especiales.'
            )

        return nombre

    def validate_apellido_usuario(self, apellido):
        if not apellido or not apellido.strip():
            raise serializers.ValidationError('El apellido no puede estar vacío.')

        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', apellido):
            raise serializers.ValidationError(
                'El apellido solo puede contener letras y espacios, sin números ni caracteres especiales.'
            )

        return apellido

    def validate_email_usuario(self, email):
        if not email or not email.strip():
            raise serializers.ValidationError('El email no puede estar vacío.')

        if '@' in email:
            raise serializers.ValidationError('El email no es valido.')

        return email