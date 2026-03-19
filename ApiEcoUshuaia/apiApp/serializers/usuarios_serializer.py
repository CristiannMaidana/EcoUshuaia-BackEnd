import re

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apiApp.models import Usuarios

User = get_user_model()


class UsuariosSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, trim_whitespace=False)

    class Meta:
        model = Usuarios
        fields = '__all__'
        read_only_fields =  ('id_usuario',)
        validators = []

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

    def validate_email(self, email):
        if not email or not email.strip():
            raise serializers.ValidationError('El email no puede estar vacío.')

        if '@' not in email:
            raise serializers.ValidationError('El email no es valido.')

        return email

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.get('email')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        validated_data['user'] = user
        return super().create(validated_data)