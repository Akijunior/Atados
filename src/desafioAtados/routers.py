from rest_framework import routers

from voluntario.views import VoluntarioViewSet
from acao.views import AcaoViewSet

router = routers.DefaultRouter()

router.register(r'voluntarios', VoluntarioViewSet, basename='voluntario')
router.register(r'acoes', AcaoViewSet, basename='acao')