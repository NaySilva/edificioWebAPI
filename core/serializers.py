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

class ProfissionalSerializer(serializers.HyperlinkedModelSerializer):

    escritorio = serializers.SlugRelatedField(queryset=Escritorio.objects.all(),
                                          slug_field="nome_escritorio")

    class Meta:
        model = Profissional
        fields = ('url', 'user', 'telefone', 'profissao', 'gerente', 'escritorio', 'status')


class ItemAgendaSerializer(serializers.HyperlinkedModelSerializer):

    profissional = serializers.SlugRelatedField(queryset=Profissional.objects.all(),
                                          slug_field="nome")
    cliente = serializers.SlugRelatedField(queryset=Cliente.objects.all(),
                                          slug_field="nome")
    escritorio = serializers.SlugRelatedField(queryset=Escritorio.objects.all(),
                                            slug_field="nome_escritorio")

    class Meta:
        model = ItemAgenda
        fields = ('url', 'profissional', 'cliente', 'data', 'horario', 'escritorio', 'situacao')


class ProfissionalDetailSerializer(serializers.HyperlinkedModelSerializer):

    escritorio = serializers.SlugRelatedField(queryset=Escritorio.objects.all(),
                                          slug_field="nome_escritorio")

    agenda = ItemAgendaSerializer(many=True, read_only=True)

    class Meta:
        model = Profissional
        fields = ('url', 'user','telefone', 'profissao', 'gerente', 'escritorio', 'status','agenda')


class EscritorioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Escritorio
        fields = ('url', 'nome_escritorio', 'servico', 'salas')


class EscritorioDetailSerializer(serializers.HyperlinkedModelSerializer):

    salas = SalaSerializer(many=True, read_only=True)

    profissionais = ProfissionalSerializer(many=True, read_only=True)

    class Meta:
        model = Escritorio
        fields = ('url', 'nome_escritorio', 'servico', 'profissionais', 'salas')


