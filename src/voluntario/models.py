from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Voluntario(models.Model):

    nome = models.CharField("Primeiro nome", max_length=20)
    sobrenome = models.CharField("Restante do nome", max_length=80)
    local = models.ForeignKey('acao.Endereco', on_delete=models.DO_NOTHING)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)