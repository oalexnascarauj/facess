from rest_framework import serializers
from .models import DadosBiometricos, ImagemFacial, TentativaReconhecimento, ConfiguracaoReconhecimento


class DadosBiometricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBiometricos
        fields = "__all__"


class ImagemFacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemFacial
        fields = "__all__"


class TentativaReconhecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TentativaReconhecimento
        fields = "__all__"


class ConfiguracaoReconhecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracaoReconhecimento
        fields = "__all__"
