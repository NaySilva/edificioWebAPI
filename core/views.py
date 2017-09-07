import json

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import *
from core.serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-list'


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    name = 'cliente-detail'


class SalaList(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    name = 'sala-list'


class SalaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    name = 'sala-detail'



class ItemAgendaList(generics.ListCreateAPIView):
    queryset = ItemAgenda.objects.all()
    serializer_class = ItemAgendaSerializer
    name = 'itemagenda-list'


class ItemAgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemAgenda.objects.all()
    serializer_class = ItemAgendaSerializer
    name = 'itemagenda-detail'


class ProfissionalList(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    name = 'profissional-list'


class ProfissionalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalDetailSerializer
    name = 'profissional-detail'




class EscritorioList(generics.ListCreateAPIView):
    queryset = Escritorio.objects.all()
    serializer_class = EscritorioSerializer
    name = 'escritorio-list'


class EscritorioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Escritorio.objects.all()
    serializer_class = EscritorioDetailSerializer
    name = 'escritorio-detail'


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
