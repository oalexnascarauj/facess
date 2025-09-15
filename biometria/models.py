from django.db import models
from django.conf import settings
from academico.models import DispositivoReconhecimento, Sala


class DadosBiometricos(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    encoding_facial = models.TextField()
    qualidade_imagem = models.FloatField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Biometria de {self.usuario}"


class ImagemFacial(models.Model):
    TIPO_CHOICES = (
        ("CADASTRO", "Cadastro"),
        ("ATUALIZACAO", "Atualização"),
        ("VERIFICACAO", "Verificação"),
    )

    dados_biometricos = models.ForeignKey(DadosBiometricos, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="biometria/imagens/")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    qualidade = models.FloatField()
    data_captura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem {self.tipo} de {self.dados_biometricos.usuario}"


class TentativaReconhecimento(models.Model):
    dispositivo = models.ForeignKey(DispositivoReconhecimento, on_delete=models.CASCADE)
    usuario_identificado = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    imagem_capturada = models.ImageField(upload_to="biometria/tentativas/")
    score_confianca = models.FloatField()
    sucesso = models.BooleanField()
    data_tentativa = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        u = self.usuario_identificado or "Desconhecido"
        return f"Tentativa {u} @ {self.sala.sigla} ({'OK' if self.sucesso else 'FALHA'})"


class ConfiguracaoReconhecimento(models.Model):
    threshold_confianca = models.FloatField(default=0.8)
    max_tentativas_por_minuto = models.PositiveIntegerField(default=10)
    timeout_reconhecimento = models.PositiveIntegerField(default=30)  # segundos
    salvar_imagens_falha = models.BooleanField(default=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"Config Reconhecimento (ativo={self.ativa})"
