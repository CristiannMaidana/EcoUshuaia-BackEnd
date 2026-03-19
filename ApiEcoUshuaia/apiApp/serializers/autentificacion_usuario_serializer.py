from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from apiApp.models import Usuarios

User = get_user_model()


class AutentificacionUsuarioSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Validar que exista el perfil y tenga user asociado
        try:
            perfil = Usuarios.objects.select_related("user").get(email=email)
        except Usuarios.DoesNotExist:
            raise serializers.ValidationError({"email": "Email o contraseña inválidos."})

        if perfil.user_id is None:
            raise serializers.ValidationError({"email": "La cuenta no tiene usuario de autenticación asociado."})

        # Autenticar
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError({"password": "Email o contraseña inválidos."})

        attrs["user"] = user
        attrs["perfil"] = perfil
        return attrs