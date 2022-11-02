from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cadastro(Base):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=13)
    cidade = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'

    def __str__(self):
        return self.nome

