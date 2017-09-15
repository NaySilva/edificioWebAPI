import json

from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse


class APITest(TestCase):

    fixtures = ['fixtures.json']

    def auth(self):
        self.client.post("/api-auth/login/", {"username": "Bret", "password": "123"})

    # Test Cliente #

    def test_cliente_list_auth(self):
        self.auth()
        response = self.client.get(reverse('cliente-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_cliente_list_unauth(self):
        response = self.client.get(reverse('cliente-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_cliente_detail_auth(self):
        self.auth()
        response = self.client.get(reverse('cliente-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_cliente_detail_unauth(self):
        response = self.client.get(reverse('cliente-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_cliente_detail_auth(self):
        self.auth()
        request_data = {'nome': 'Joana',
                         'telefone': '32242443',
                         'cpf': '99999'}
        response = self.client.post(reverse('cliente-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_cliente_detail_unauth(self):
        request_data = {'nome': 'Joana',
                         'telefone': '32242443',
                         'cpf': '99999'}
        response = self.client.post(reverse('cliente-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_delete_cliente_auth(self):
        self.auth()
        response = self.client.delete(reverse('cliente-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_cliente_unauth(self):
        response = self.client.delete(reverse('cliente-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_cliente_auth(self):
        self.auth()
        request_data = {"nome": "Maria",
                        "telefone": '32222222',
                        'cpf': "11111"}
        response = self.client.put(reverse('cliente-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_cliente_unauth(self):
        request_data = {"nome": "Maria",
                        "telefone": '32222222',
                        'cpf': "11111"}
        response = self.client.put(reverse('cliente-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # End Test Cliente #

    # Test Profissional #

    def test_profissional_list_auth(self):
        self.auth()
        response = self.client.get(reverse('profissional-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_profissional_list_unauth(self):
        response = self.client.get(reverse('profissional-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_profissional_detail_auth(self):
        self.auth()
        response = self.client.get(reverse('profissional-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_profissional_detail_unauth(self):
        response = self.client.get(reverse('profissional-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_profissional_detail_auth(self):
        self.auth()
        request_data = {'user': reverse('user-detail', args=[2]),
                         'telefone': '32242443',
                         'profissao': 'Dentista',
                        'escritorio': reverse('escritorio-detail', args=[1])}
        response = self.client.post(reverse('profissional-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


    def test_create_profissional_detail_unauth(self):
        request_data = {'user': reverse('user-detail', args=[2]),
                         'telefone': '32242443',
                         'profissao': 'Dentista',
                        'escritorio': reverse('escritorio-detail', args=[1])}
        response = self.client.post(reverse('profissional-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_delete_profissional_auth(self):
        self.auth()
        response = self.client.delete(reverse('profissional-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_profissional_unauth(self):
        response = self.client.delete(reverse('profissional-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_update_profissional_unauth(self):
        request_data = {'user': reverse('user-detail', args=[1]),
                        'telefone': '32242443',
                        'profissao': 'Dentista',
                        'escritorio': reverse('escritorio-detail', args=[1])}
        response = self.client.put(reverse('profissional-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # End Test Profissional #

    # Test Escritorio #

    def test_escritorio_list_auth(self):
        self.auth()
        response = self.client.get(reverse('escritorio-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_escritorio_list_unauth(self):
        response = self.client.get(reverse('escritorio-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_escritorio_detail_auth(self):
        self.auth()
        response = self.client.get(reverse('escritorio-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_escritorio_detail_unauth(self):
        response = self.client.get(reverse('escritorio-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_escritorio_detail_unauth(self):
        request_data = {'nome_escritorio': 'Dermat',
                         'servico': 'Dermatologia'}
        response = self.client.post(reverse('escritorio-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_delete_escritorio_auth(self):
        self.auth()
        response = self.client.delete(reverse('escritorio-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_escritorio_unauth(self):
        response = self.client.delete(reverse('escritorio-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_escritorio_auth(self):
        self.auth()
        request_data = {'nome_escritorio': 'Dermat',
                         'servico': 'Dermatologia'}
        response = self.client.put(reverse('escritorio-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_escritorio_unauth(self):
        request_data = {'nome_escritorio': 'Dermat',
                         'servico': 'Dermatologia'}
        response = self.client.put(reverse('escritorio-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # End Test Escritorio #


    # Test Sala #

    def test_01_sala_list_auth(self):
        self.auth()
        response = self.client.get(reverse('sala-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_02_sala_list_unauth(self):
        response = self.client.get(reverse('sala-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_03_sala_detail_auth(self):
        self.auth()
        response = self.client.get(reverse('sala-detail', args=[3]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_04_sala_detail_unauth(self):
        response = self.client.get(reverse('sala-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_05_create_sala_detail_auth(self):
        self.auth()
        request_data = {'numero': '3', 'andar': '1', 'escritorio': reverse('escritorio-detail',args=[1])}
        response = self.client.post(reverse('sala-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


    def test_06_create_sala_detail_unauth(self):
        request_data = {'numero': '3',
                         'andar': '1',
                        'escritorio': reverse('escritorio-detail',args=[1])}
        response = self.client.post(reverse('sala-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_07_delete_sala_auth(self):
        self.auth()
        response = self.client.delete(reverse('sala-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_08_delete_sala_unauth(self):
        response = self.client.delete(reverse('sala-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_09_update_sala_auth(self):
        self.auth()
        request_data = {'numero': '3',
                         'andar': '1',
                        'escritorio': reverse('escritorio-detail',args=[1])}
        response = self.client.put(reverse('sala-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_10_update_sala_unauth(self):
        request_data = {'numero': '3',
                         'andar': '1',
                        'escritorio': reverse('escritorio-detail',args=[1])}
        response = self.client.put(reverse('sala-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # End Test Sala #

    # Test Agenda #

    def test_agenda_list_auth(self):
        self.auth()
        response = self.client.get(reverse('itemagenda-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_agenda_list_unauth(self):
        response = self.client.get(reverse('itemagenda-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_agenda_detail_auth(self):
        self.auth()
        response = self.client.get(reverse('itemagenda-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_agenda_detail_unauth(self):
        response = self.client.get(reverse('itemagenda-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_agenda_detail_auth(self):
        self.auth()
        request_data = {'profissional': reverse('profissional-detail', args=[1]),
                        'cliente': reverse('cliente-detail', args=[1]),
                        'data': '2017-09-01',
                        'horario': '9:00'}
        response = self.client.post(reverse('itemagenda-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_agenda_detail_unauth(self):
        request_data = {'profissional': reverse('profissional-detail', args=[1]),
                        'cliente': reverse('cliente-detail', args=[1]),
                        'data': '2017-09-01',
                        'horario': '9:00'}
        response = self.client.post(reverse('itemagenda-list'), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_delete_agenda_auth(self):
        self.auth()
        response = self.client.delete(reverse('itemagenda-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_agenda_unauth(self):
        response = self.client.delete(reverse('itemagenda-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_agenda_auth(self):
        self.auth()
        request_data = {'profissional': reverse('profissional-detail', args=[1]),
                        'cliente': reverse('cliente-detail', args=[1]),
                        'data': '2017-09-01',
                        'horario': '9:00'}
        response = self.client.put(reverse('itemagenda-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_agenda_unauth(self):
        request_data = {'profissional': reverse('profissional-detail', args=[1]),
                        'cliente': reverse('cliente-detail', args=[1]),
                        'data': '2017-09-01',
                        'horario': '9:00'}
        response = self.client.put(reverse('itemagenda-detail', args=[1]), json.dumps(request_data), 'application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # End Test Agenda #
