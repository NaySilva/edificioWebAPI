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


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-list'
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome','cpf')

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class SalaList(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    name = 'sala-list'
    throttle_scope = 'salas'
    throttle_classes = (ScopedRateThrottle,)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSalaOrReadOnly,
    )


class SalaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    name = 'sala-detail'
    throttle_scope = 'salas'
    throttle_classes = (ScopedRateThrottle,)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSalaOrReadOnly,
    )



class ItemAgendaList(generics.ListCreateAPIView):
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
    queryset = ItemAgenda.objects.all()
    serializer_class = ItemAgendaSerializer
    name = 'itemagenda-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsItemAgendaOrReadOnly,
    )


class ProfissionalList(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    name = 'profissional-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsProfissionalOrReadOnly,
    )


class ProfissionalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalDetailSerializer
    name = 'profissional-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsProfissionalOrReadOnly,
    )


class EscritorioList(generics.ListCreateAPIView):
    queryset = Escritorio.objects.all()
    serializer_class = EscritorioSerializer
    name = 'escritorio-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsEscritorioOrReadOnly,
    )


class EscritorioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Escritorio.objects.all()
    serializer_class = EscritorioDetailSerializer
    name = 'escritorio-detail'

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
