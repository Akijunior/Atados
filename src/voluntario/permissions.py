from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class CustomForbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Apenas o próprio usuário pode editar essa conta"

class OnlyTheOwnUserCanEditHimself(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        web_token = request.META.get('HTTP_AUTHORIZATION', None)
        token = Token.objects.filter(key=web_token).last()
        if not token.user == obj:
            raise CustomForbidden
        return True
