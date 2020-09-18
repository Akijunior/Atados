from django.db import models

# Create your models here.
class Endereco(models.Model):

    cidade = models.CharField("Cidade em que reside", max_length=80)
    bairro = models.CharField("Bairro em que reside", max_length=80)
    endereco = models.CharField("Endereço em que reside", max_length=80, null=True, blank=True)

class Acao(models.Model):

    nome = models.CharField("Nome da ação", max_length=100)
    instituicao = models.CharField("Nome da instituição que está organizando", max_length=100)
    cidade = models.CharField("Cidade em que reside", max_length=80)
    bairro = models.CharField("Bairro em que reside", max_length=80)
    endereco = models.CharField("Endereço em que reside", max_length=80, null=True, blank=True)

    class Meta:

        ordering = ["nome", "instituicao"]