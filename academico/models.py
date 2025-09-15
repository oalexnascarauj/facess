from django.db import models
from django.conf import settings


class Escola(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    endereco = models.TextField(blank=True)
    ativa = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class Curso(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ("escola", "codigo")

    def __str__(self):
        return f"{self.nome} - {self.codigo}"


class UnidadeCurricular(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50)
    ativa = models.BooleanField(default=True)

    class Meta:
        unique_together = ("curso", "codigo")

    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class Serie(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    ativa = models.BooleanField(default=True)

    class Meta:
        unique_together = ("curso", "nome")

    def __str__(self):
        return f"{self.curso.codigo} - {self.nome}"


class Turno(models.Model):
    nome = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    sigla = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=200, blank=True)
    capacidade = models.PositiveIntegerField(null=True, blank=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.sigla


class DispositivoReconhecimento(models.Model):
    STATUS_CHOICES = (
        ("ONLINE", "Online"),
        ("OFFLINE", "Offline"),
        ("MANUTENCAO", "Manutenção"),
    )

    nome = models.CharField(max_length=100)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    ip_endereco = models.GenericIPAddressField()
    porta = models.PositiveIntegerField(default=80)
    modelo = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OFFLINE")
    ativo = models.BooleanField(default=True)
    data_instalacao = models.DateTimeField()
    ultima_comunicacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.sala.sigla})"


class HorarioAula(models.Model):
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    professor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    dia_semana = models.IntegerField()  # 0-6 seg-dom
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["sala", "dia_semana", "horario_inicio"]),
        ]

    def __str__(self):
        return f"{self.unidade_curricular.codigo} {self.dia_semana} {self.horario_inicio}-{self.horario_fim}"
