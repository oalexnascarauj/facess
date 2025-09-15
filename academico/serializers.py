from rest_framework import serializers
from .models import (
    Escola,
    Curso,
    UnidadeCurricular,
    Serie,
    Turno,
    Sala,
    DispositivoReconhecimento,
    HorarioAula,
)


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class UnidadeCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCurricular
        fields = "__all__"


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = "__all__"


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = "__all__"


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = """id escola sigla descricao capacidade ativa""".split()


class DispositivoReconhecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoReconhecimento
        fields = "__all__"


class HorarioAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioAula
        fields = "__all__"
