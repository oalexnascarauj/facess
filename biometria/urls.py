from rest_framework.routers import DefaultRouter
from .views import (
    DadosBiometricosViewSet,
    ImagemFacialViewSet,
    TentativaReconhecimentoViewSet,
    ConfiguracaoReconhecimentoViewSet,
)


router = DefaultRouter()
router.register(r"biometria/dados", DadosBiometricosViewSet)
router.register(r"biometria/imagens", ImagemFacialViewSet)
router.register(r"biometria/tentativas", TentativaReconhecimentoViewSet)
router.register(r"biometria/configuracoes", ConfiguracaoReconhecimentoViewSet)

urlpatterns = router.urls
