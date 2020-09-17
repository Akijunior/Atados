from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status


class BaseViewTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='3',
                                                         password='12test12',
                                                         email='test@example.com')
        print(Token.objects.all())
        self.token = Token.objects.get(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.login(username='3', password='12test12')

    def tearDown(self):
        self.client.logout()


class UserViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = {
            "email": 'a@a.com',
            "password": '12test12',
            "password2": '12test12',
        }

    def test_criar_usuario_com_sucesso(self):
        response = self.client.post('/api/v1/criar-usuario/', self.user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_nao_pode_criar_dois_usuarios_com_mesmo_email(self):
        response = self.client.post('/api/v1/criar-usuario/', self.user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('/api/v1/criar-usuario/', self.user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nao_pode_criar_usuario_caso_a_primeira_senha_seja_diferente_da_segunda(self):
        self.user["password2"] = "outra-senha"
        response = self.client.post('/api/v1/criar-usuario/', self.user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nao_pode_criar_usuario_com_senha_com_menos_de_4_caracteres(self):
        self.user["password"] = "out"
        self.user["password2"] = "out"
        response = self.client.post('/api/v1/criar-usuario/', self.user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        User.objects.all().delete()
