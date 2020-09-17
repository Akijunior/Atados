from rest_framework import serializers

from voluntario.models import Voluntario

from .models import Acao


class AcaoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acao
        fields = '__all__'