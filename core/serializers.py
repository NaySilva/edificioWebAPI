from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email')


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('url', 'nome', 'telefone', 'cpf')


class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = ('url', 'numero', 'andar')


class ItemAgendaSerializer(serializers.HyperlinkedModelSerializer):

    profissional = serializers.SlugRelatedField(queryset=Profissional.objects.all(),
                                          slug_field="nome")
    cliente = serializers.SlugRelatedField(queryset=Cliente.objects.all(),
                                          slug_field="nome")

    class Meta:
        model = ItemAgenda
        fields = ('url', 'profissional', 'cliente', 'data', 'horario')



class ProfissionalSerializer(serializers.HyperlinkedModelSerializer):

    escritorio = serializers.SlugRelatedField(queryset=Escritorio.objects.all(),
                                          slug_field="nome_escritorio")
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field="username")

    class Meta:
        model = Profissional
        fields = ('url', 'user', 'telefone', 'profissao', 'gerente', 'escritorio', 'status',)

class ProfissionalDetailSerializer(serializers.HyperlinkedModelSerializer):

    escritorio = serializers.SlugRelatedField(queryset=Escritorio.objects.all(),
                                          slug_field="nome_escritorio")
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field="username")

    agenda_profissional = ItemAgendaSerializer(many=True, read_only=True)

    class Meta:
        model = Profissional
        fields = ('url', 'user','telefone', 'profissao', 'gerente', 'escritorio', 'status', 'agenda_profissional')


class EscritorioSerializer(serializers.HyperlinkedModelSerializer):

    salas = serializers.SlugRelatedField(many=True, queryset=Sala.objects.all(), slug_field="descricao")

    class Meta:
        model = Escritorio
        fields = ('url', 'nome_escritorio', 'servico', 'salas')


class EscritorioDetailSerializer(serializers.HyperlinkedModelSerializer):

    salas = serializers.SlugRelatedField(many=True, queryset=Sala.objects.all(), slug_field="descricao")

    profissionais = ProfissionalSerializer(many=True, read_only=True)

    class Meta:
        model = Escritorio
        fields = ('url', 'nome_escritorio', 'servico', 'profissionais', 'salas')


