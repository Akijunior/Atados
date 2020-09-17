from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers, status
from rest_framework.exceptions import APIException
from django.db import IntegrityError

from .models import Voluntario

VALIDATE_VALID_EMAIL_REGEX = True
EMAIL_VALIDATE_REGEX = r"[^@]+@[^@]+\.[^@]+"
MIN_PASSWORD_LENGHT = 4


class VoluntarioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voluntario
        fields = "__all__"


class Custom409(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Já existe um usuário cadastrado com o e-mail em questão."


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label="Senha", max_length=30, style={'input_type': 'password'},
                                     write_only=True, required=False)
    password2 = serializers.CharField(label="Confirmação da senha", max_length=30,
                                      style={'input_type': 'password'},
                                      write_only=True, required=False)
    email = serializers.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, data):
        errors = dict()

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)

    def validate_senha(self, senha1, senha2):
        if len(senha1) < MIN_PASSWORD_LENGHT:
            raise serializers.ValidationError(f"A senha deve ter {MIN_PASSWORD_LENGHT} caracteres ou mais")
        if (senha1 != senha2):
            raise serializers.ValidationError("A primeira senha não coincide com a segunda.")
        return senha1

    def validate_email(self, email):
        if User.objects.filter(Q(email=email) | Q(username=email)).exists():
            raise serializers.ValidationError("Já existe um usuário cadastrado com este e-mail")

        return email

    def create(self, validated_data):
        try:
            senha2 = validated_data.pop('password2')
            validated_data['password'] = self.validate_senha(validated_data['password'], senha2)
            validated_data['username'] = validated_data['email']
            auth_usuario = User.objects.create_user(**validated_data)

            auth_usuario.save()

            return User.objects.get(id=auth_usuario.id)

        except IntegrityError as exception:
            raise Custom409(exception)
