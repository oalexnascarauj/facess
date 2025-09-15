from rest_framework.routers import DefaultRouter
from .views import (
    CustomUserViewSet,
    PerfilAcessoViewSet,
    PermissaoViewSet,
    PerfilPermissaoViewSet,
    UsuarioPerfilViewSet,
)


router = DefaultRouter()
router.register(r"usuarios", CustomUserViewSet)
router.register(r"perfis", PerfilAcessoViewSet)
router.register(r"permissoes", PermissaoViewSet)
router.register(r"perfil-permissoes", PerfilPermissaoViewSet)
router.register(r"usuario-perfis", UsuarioPerfilViewSet)

urlpatterns = router.urls
