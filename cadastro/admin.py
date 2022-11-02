from django.contrib import admin
from .models import Cadastro


@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_dislplay = ('nome', 'email', 'telefone', 'cidade', 'criacao')
