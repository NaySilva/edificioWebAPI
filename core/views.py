import json

from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle

from core.models import *
from core.permissions import *
from core.serializers import *


class UserList(generics.ListAPIView):
    """
     get: Retorna uma lista de todos os usuarios
     """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    get: Mostra um usuário especifico
    put: Atualiza um usuário especifico
    delete: Atualiza um usuário especifico
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    http_method_names = ['get','put','delete', 'head','options']

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )


class ClienteList(generics.ListCreateAPIView):
    '''
    get: Retorna uma lista todos os clientes
    post: Cria um novo cliente
    '''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-list'
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome','cpf')


    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    get: Mostra o cliente especifico
    put: Atualiza um cliente especifico
    delete: Deleta um cliente especifico
    '''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-detail'
    http_method_names = ['get', 'delete', 'post', 'put','head','options']

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class SalaList(generics.ListAPIView):
    '''
    get: Retorna uma lista de todas as salas cadastradas
    '''
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    name = 'sala-list'
    throttle_scope = 'salas'
    throttle_classes = (ScopedRateThrottle,)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSalaOrReadOnly,
    )


class SalaDetail(generics.RetrieveAPIView):
    '''
    get: Mostra a sala especifica
    '''
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    name = 'sala-detail'
    http_method_names = ['get','head','options']
    throttle_scope = 'salas'
    throttle_classes = (ScopedRateThrottle,)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSalaOrReadOnly,
    )



class ItemAgendaList(generics.ListCreateAPIView):
    '''
    get: Retorna uma lista de todas os compromissos agendados
    post: Agenda um novo compromisso
    '''
    queryset = ItemAgenda.objects.all()
    serializer_class = ItemAgendaSerializer
    name = 'itemagenda-list'
    filter_backends = (OrderingFilter,)
    ordering_fields = ('data', 'horario')

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsItemAgendaOrReadOnly,
    )


class ItemAgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    get: Mostra o compromisso especifico que foi agendado
    put: Atualiza o compromisso especifico
    delete: Deleta o compromisso especifico
    '''
    queryset = ItemAgenda.objects.all()
    serializer_class = ItemAgendaSerializer
    name = 'itemagenda-detail'
    http_method_names = ['get', 'delete', 'post', 'put','head','options']

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsItemAgendaOrReadOnly,
    )


class ProfissionalList(generics.ListAPIView):
    '''
    get: Retorna uma lista de profissionais cadastrados
    '''
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    name = 'profissional-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsProfissionalOrReadOnly,
    )


class ProfissionalDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    get: Mostra o profissional especifico
    put: Atualiza o profissional especifico
    delete: Deleta o profissional especifico
    '''
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalDetailSerializer
    name = 'profissional-detail'
    http_method_names = ['get', 'delete', 'put','head','options']

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsProfissionalOrReadOnly,
    )


class EscritorioList(generics.ListCreateAPIView):
    '''
    get: Retorna uma lista de escritorios cadastrados
    post: Cria um novo escritorio
    '''
    queryset = Escritorio.objects.all()
    serializer_class = EscritorioSerializer
    name = 'escritorio-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsEscritorioOrReadOnly,
    )


class EscritorioDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    get: Mostra o escritorio especifico
    put: Atualiza o escritorio especifico
    delete: Deleta o escritorio especifico
    '''
    queryset = Escritorio.objects.all()
    serializer_class = EscritorioDetailSerializer
    name = 'escritorio-detail'
    http_method_names = ['get', 'delete', 'post', 'put','head','options']

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsEscritorioOrReadOnly,
    )


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({
            'users': reverse(UserList.name,
                            request=request),
            'clientes': reverse(ClienteList.name,
                                       request=request),
            'profissionais': reverse(ProfissionalList.name,
                             request=request),
            'escritorios': reverse(EscritorioList.name,
                             request=request),
            'salas': reverse(SalaList.name,
                             request=request),
            'agenda': reverse(ItemAgendaList.name,
                             request=request)
            })


def import_data():
    dump_data = open('db.json', 'r')
    as_json = json.load(dump_data)

    for user in as_json['users']:

        first_name = user['name'].split(" ")[0]
        last_name = user['name'].split(" ")[1]
        new_user = User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=user['username'],
                                            email=user['email'],
                                            password='123')
