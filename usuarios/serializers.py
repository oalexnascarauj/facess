from rest_framework import serializers
from .models import CustomUser, PerfilAcesso, Permissao, PerfilPermissao, UsuarioPerfil


class PerfilAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilAcesso
        fields = "__all__"


class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = "__all__"


class PerfilPermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilPermissao
        fields = "__all__"


class UsuarioPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPerfil
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password",)
