from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from acao.models import Acao
from acao.serializers import AcaoListSerializer


class AcaoViewSet(viewsets.ModelViewSet):

    queryset = Acao.objects.all()
    serializer_class = AcaoListSerializer
    permission_classes = [permissions.IsAuthenticated, ]