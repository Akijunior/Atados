from rest_framework import routers

from voluntario.views import VoluntarioViewSet, UserViewSet

from acao.views import AcaoViewSet

router = routers.DefaultRouter()

router.register(r'voluntarios', VoluntarioViewSet, basename='voluntario')
router.register(r'acoes', AcaoViewSet, basename='acao')
router.register(r'criar-usuario', UserViewSet, basename='criar_usuario')