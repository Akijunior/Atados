from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient


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

        self.partner = {}
        self.cover = {}

    def tearDown(self):
        self.client.logout()