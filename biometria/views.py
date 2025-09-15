from rest_framework import viewsets, permissions
from .models import DadosBiometricos, ImagemFacial, TentativaReconhecimento, ConfiguracaoReconhecimento
from .serializers import (
    DadosBiometricosSerializer,
    ImagemFacialSerializer,
    TentativaReconhecimentoSerializer,
    ConfiguracaoReconhecimentoSerializer,
)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class DadosBiometricosViewSet(BaseViewSet):
    queryset = DadosBiometricos.objects.all()
    serializer_class = DadosBiometricosSerializer


class ImagemFacialViewSet(BaseViewSet):
    queryset = ImagemFacial.objects.all()
    serializer_class = ImagemFacialSerializer


class TentativaReconhecimentoViewSet(BaseViewSet):
    queryset = TentativaReconhecimento.objects.all()
    serializer_class = TentativaReconhecimentoSerializer


class ConfiguracaoReconhecimentoViewSet(BaseViewSet):
    queryset = ConfiguracaoReconhecimento.objects.all()
    serializer_class = ConfiguracaoReconhecimentoSerializer
