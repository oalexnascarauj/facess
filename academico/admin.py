from django.contrib import admin
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


admin.site.register(Escola)
admin.site.register(Curso)
admin.site.register(UnidadeCurricular)
admin.site.register(Serie)
admin.site.register(Turno)
admin.site.register(Sala)
admin.site.register(DispositivoReconhecimento)
admin.site.register(HorarioAula)
