from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    TIPO_CHOICES = (
        ("ALUNO", "Aluno"),
        ("PROFESSOR", "Professor"),
        ("SECRETARIA", "Secretária"),
        ("COORDENACAO", "Coordenação"),
        ("ADMIN", "Admin"),
    )

    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto_perfil = models.ImageField(upload_to="perfil/", blank=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_CHOICES, default="ALUNO")

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"


class PerfilAcesso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Permissao(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class PerfilPermissao(models.Model):
    perfil = models.ForeignKey(PerfilAcesso, on_delete=models.CASCADE)
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE)
    data_atribuicao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("perfil", "permissao")

    def __str__(self):
        return f"{self.perfil} -> {self.permissao}"


class UsuarioPerfil(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    perfil = models.ForeignKey(PerfilAcesso, on_delete=models.CASCADE)
    data_atribuicao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ("usuario", "perfil")

    def __str__(self):
        return f"{self.usuario} -> {self.perfil}"
