from django.contrib import admin
from .models import DadosBiometricos, ImagemFacial, TentativaReconhecimento, ConfiguracaoReconhecimento


admin.site.register(DadosBiometricos)
admin.site.register(ImagemFacial)
admin.site.register(TentativaReconhecimento)
admin.site.register(ConfiguracaoReconhecimento)
