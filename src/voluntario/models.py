from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Voluntario(models.Model):

    nome = models.CharField("Primeiro nome", max_length=20)
    sobrenome = models.CharField("Restante do nome", max_length=80)
    cidade = models.CharField("Cidade em que reside", max_length=80)
    bairro = models.CharField("Bairro em que reside", max_length=80)

    class Meta:

        ordering = ["nome", ]

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)