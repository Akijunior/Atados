from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from acao.models import Acao
from acao.serializers import AcaoListSerializer


class AcaoViewSet(viewsets.ModelViewSet):

    queryset = Acao.objects.all()
    serializer_class = AcaoListSerializer

    user_actions = ['create', 'destroy']
    safe_actions = ['list', 'retrieve']

    def get_permissions(self):
        if self.action in self.user_actions:
            self.permission_classes = [permissions.IsAuthenticated, ]
        else:
            self.permission_classes = [permissions.AllowAny, ]

        return super(self.__class__, self).get_permissions()
