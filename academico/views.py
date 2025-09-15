from rest_framework import viewsets, permissions
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
from .serializers import (
    EscolaSerializer,
    CursoSerializer,
    UnidadeCurricularSerializer,
    SerieSerializer,
    TurnoSerializer,
    SalaSerializer,
    DispositivoReconhecimentoSerializer,
    HorarioAulaSerializer,
)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class EscolaViewSet(BaseViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer


class CursoViewSet(BaseViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class UnidadeCurricularViewSet(BaseViewSet):
    queryset = UnidadeCurricular.objects.all()
    serializer_class = UnidadeCurricularSerializer


class SerieViewSet(BaseViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class TurnoViewSet(BaseViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


class SalaViewSet(BaseViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class DispositivoReconhecimentoViewSet(BaseViewSet):
    queryset = DispositivoReconhecimento.objects.all()
    serializer_class = DispositivoReconhecimentoSerializer


class HorarioAulaViewSet(BaseViewSet):
    queryset = HorarioAula.objects.all()
    serializer_class = HorarioAulaSerializer
