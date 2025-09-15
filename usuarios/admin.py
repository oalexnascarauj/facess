from django.contrib import admin
from .models import CustomUser, PerfilAcesso, Permissao, PerfilPermissao, UsuarioPerfil


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "cpf", "tipo_usuario", "ativo")
    search_fields = ("username", "first_name", "last_name", "cpf")
    list_filter = ("tipo_usuario", "ativo")


@admin.register(PerfilAcesso)
class PerfilAcessoAdmin(admin.ModelAdmin):
    list_display = ("nome", "ativo", "data_criacao")
    search_fields = ("nome",)
    list_filter = ("ativo",)


@admin.register(Permissao)
class PermissaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "ativa")
    search_fields = ("nome", "codigo")
    list_filter = ("ativa",)


@admin.register(PerfilPermissao)
class PerfilPermissaoAdmin(admin.ModelAdmin):
    list_display = ("perfil", "permissao", "data_atribuicao")
    search_fields = ("perfil__nome", "permissao__nome", "permissao__codigo")


@admin.register(UsuarioPerfil)
class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "perfil", "ativo", "data_atribuicao")
    search_fields = ("usuario__username", "usuario__first_name", "usuario__last_name", "perfil__nome")
    list_filter = ("ativo",)
