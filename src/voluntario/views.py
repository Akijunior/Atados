from django.contrib.auth.models import User

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from voluntario.models import Voluntario
from voluntario.permissions import OnlyTheOwnUserCanEditHimself
from voluntario.serializers import VoluntarioListSerializer, UserSerializer


class VoluntarioViewSet(viewsets.ModelViewSet):

    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioListSerializer

    user_actions = ['create', 'destroy']
    safe_actions = ['list', 'retrieve']

    def get_permissions(self):
        if self.action in self.user_actions:
            self.permission_classes = [permissions.IsAuthenticated, ]
        else:
            self.permission_classes = [permissions.AllowAny, ]

        return super(self.__class__, self).get_permissions()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [OnlyTheOwnUserCanEditHimself, ]

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [OnlyTheOwnUserCanEditHimself, ]

        return super(self.__class__, self).get_permissions()


    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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