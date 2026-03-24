import re

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from apiApp.models import Usuarios

User = get_user_model()


class UsuariosSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only=True, required=False, trim_whitespace=False)
    password = serializers.CharField(write_only=True, required=False, trim_whitespace=False)

    class Meta:
        model = Usuarios
        fields = '__all__'
        read_only_fields = ('id_usuario', 'user')
        validators = []

    def validate(self, attrs):
        if self.instance is None and not attrs.get('password'):
            raise serializers.ValidationError({'password': 'La contraseña es obligatoria.'})

        if self.instance is not None and attrs.get('password'):
            current_password = attrs.get('current_password')
            auth_user = self.instance.user

            if auth_user is None:
                raise serializers.ValidationError(
                    {'password': 'El perfil no tiene un usuario autenticable asociado.'}
                )

            if not current_password:
                raise serializers.ValidationError(
                    {'current_password': 'Debes ingresar tu contraseña actual para cambiarla.'}
                )

            if not auth_user.check_password(current_password):
                raise serializers.ValidationError(
                    {'current_password': 'La contraseña actual es incorrecta.'}
                )

        return attrs

    def validate_nombre_usuario(self, nombre):
        if not nombre or not nombre.strip():
            raise serializers.ValidationError('El nombre no puede estar vacío.')

        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre):
            raise serializers.ValidationError(
                'El nombre solo puede contener letras y espacios, sin números ni caracteres especiales.'
            )

        return nombre.strip()

    def validate_apellido_usuario(self, apellido):
        if not apellido or not apellido.strip():
            raise serializers.ValidationError('El apellido no puede estar vacío.')

        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', apellido):
            raise serializers.ValidationError(
                'El apellido solo puede contener letras y espacios, sin números ni caracteres especiales.'
            )

        return apellido.strip()

    def validate_email(self, email):
        if not email or not email.strip():
            raise serializers.ValidationError('El email no puede estar vacío.')

        email = email.strip().lower()

        if '@' not in email:
            raise serializers.ValidationError('El email no es valido.')

        return email

    @transaction.atomic
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

    @transaction.atomic
    def update(self, instance, validated_data):
        validated_data.pop('current_password', None)
        password = validated_data.pop('password', None)
        email = validated_data.get('email')
        auth_user = instance.user

        if auth_user is not None:
            if email:
                auth_user.email = email
                auth_user.username = email

            if password:
                auth_user.set_password(password)

            if email or password:
                auth_user.save()

        return super().update(instance, validated_data)
