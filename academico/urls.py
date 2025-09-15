from rest_framework.routers import DefaultRouter
from .views import (
    EscolaViewSet,
    CursoViewSet,
    UnidadeCurricularViewSet,
    SerieViewSet,
    TurnoViewSet,
    SalaViewSet,
    DispositivoReconhecimentoViewSet,
    HorarioAulaViewSet,
)


router = DefaultRouter()
router.register(r"escolas", EscolaViewSet)
router.register(r"cursos", CursoViewSet)
router.register(r"unidades-curriculares", UnidadeCurricularViewSet)
router.register(r"series", SerieViewSet)
router.register(r"turnos", TurnoViewSet)
router.register(r"salas", SalaViewSet)
router.register(r"dispositivos", DispositivoReconhecimentoViewSet)
router.register(r"horarios-aula", HorarioAulaViewSet)

urlpatterns = router.urls
