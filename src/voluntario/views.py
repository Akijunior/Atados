from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, permissions

from voluntario.models import Voluntario
from voluntario.serializers import VoluntarioListSerializer


class VoluntarioViewSet(viewsets.ModelViewSet):

    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioListSerializer
    permission_classes = [permissions.IsAuthenticated, ]