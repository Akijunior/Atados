from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from acao.models import Acao
from acao.serializers import AcaoListSerializer


class AcaoViewSet(viewsets.ModelViewSet):

    queryset = Acao.objects.all()
    serializer_class = AcaoListSerializer

    user_actions = ['create', 'destroy', 'update']
    safe_actions = ['list', 'retrieve']

    def get_permissions(self):
        if self.action in self.user_actions:
            self.permission_classes = [permissions.IsAuthenticated, ]
        else:
            self.permission_classes = [permissions.AllowAny, ]

        return super(self.__class__, self).get_permissions()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
