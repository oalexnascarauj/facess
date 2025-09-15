from rest_framework import viewsets, permissions
from .models import CustomUser, PerfilAcesso, Permissao, PerfilPermissao, UsuarioPerfil
from .serializers import (
    CustomUserSerializer,
    PerfilAcessoSerializer,
    PermissaoSerializer,
    PerfilPermissaoSerializer,
    UsuarioPerfilSerializer,
)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PerfilAcessoViewSet(viewsets.ModelViewSet):
    queryset = PerfilAcesso.objects.all()
    serializer_class = PerfilAcessoSerializer
    permission_classes = [IsAdminOrReadOnly]


class PermissaoViewSet(viewsets.ModelViewSet):
    queryset = Permissao.objects.all()
    serializer_class = PermissaoSerializer
    permission_classes = [IsAdminOrReadOnly]


class PerfilPermissaoViewSet(viewsets.ModelViewSet):
    queryset = PerfilPermissao.objects.all()
    serializer_class = PerfilPermissaoSerializer
    permission_classes = [IsAdminOrReadOnly]


class UsuarioPerfilViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPerfil.objects.all()
    serializer_class = UsuarioPerfilSerializer
    permission_classes = [IsAdminOrReadOnly]
