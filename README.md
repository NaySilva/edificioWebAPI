# EdificioWebAPI
Neste relatório está descrito como foi realizado cada atividade do projeto web api, cujo o modelo escolhido foi um
 sistema de agendamento de consultas dos escritórios profissionais de um edifício.

## Atividades

1. A  API  deve  possuir  pelo  menos  4  entidades  relevantes  e  relacionadas  via mapeamento objeto relacional

O diagrama abaixo representa as 6 entidades do modelo escolhido:```Sala```, ```Escritorio```, ```User```, ```Cliente```,
```ItemAgenda``` e ```Profissional```.
A classe User é do modelo padrão  ```django.contrib.auth```.

![diagrama de classes](/imagens/edifício.png)

Na classe ```ItemAgenda``` em ```models.py``` foi colocado a opção ordering para que sempre que for listada os itens da 
agenda, a ordem padrão será ascendente em relação a data e em segundo critério pelo horário.

```python
 class Meta:  
    ordering = ('data', 'horario',)  

```

2. Pelo menos uma entidade deve ser integrada ao esquema de autenticação do Django

Como a classe ```User``` é do modelo padrão  ```django.contrib.auth``` e está relacionada com a classe ```Profissional```,
 essa entidade está integrada ao esquema de autenticação, onde para realizar algumas funcionalidades o profissional 
 deverá realizar login.
 
 Veja o atributo de relacionamento entre estas entidades:
```python
class Profissional(models.Model):  
    user = models.ForeignKey('auth.User',default='1')  
```

3. Parte da API deve ser somente leitura e parte deve ser acessível apenas para usuários autenticados

Quando o usuário não é identificado qualquer entidade poderá ser visualizada. Para realizar outras tarefas como editar,
 criar ou deletar o usuário deverá ser identificado. Mas essa regra não cabe a todas as entidades. Algumas entidades 
 como ```Sala```, não poderá ser editada, criada ou deletada pelo usuário, mesmo estando autenticado. Outros requisitos 
 mais específicos foram desenvolvidos em algumas entidade como o do ```Profissional```, onde ele só poderá editar ou 
 excluir se estiver relacionada a ele, ou seja se a instância do ```Profissional``` for do usuário autenticado. 
A tabela mostra as tarefas permitidas pelos usuário autenticados ou não.

![tabela](/imagens/tabela.png)

Para restringir essas entidades foram adicionadas nas suas views permissões, no arquivo view.py. A restrição de usuários
 não autenticados acontece pela classe ```rest_framework.permissions.IsAuthenticatedOrReadOnly```. Para  exemplificar, 
 a view profissional descrita abaixo tem as seguintes permissões:

```python
permission_classes = (  
    permissions.IsAuthenticatedOrReadOnly,  
    IsProfissionalOrReadOnly,  
 )   
```

A permissão ```IsProfissionalOrReadOnly``` é serve para usuários autenticados e está restrigida no arquivo 
permissions.py que tem o seguinte codigo:

```python
class IsProfissionalOrReadOnly(permissions.BasePermission):  
    def has_object_permission(self, request, view, obj):  
        if request.method in permissions.SAFE_METHODS:  
            return True  
        else:  
            return obj.user == request.user  
```

Para essas permissões funcionarem, as classes devem ser informadas na variável de configuração do Django Rest Framework 
no arquivo settings.py. Veja como foi configurada neste projeto:

```python
 REST_FRAMEWORK = {  
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',  
    'PAGE_SIZE': 5,  
    'DEFAULT_AUTHENTICATION_CLASSES':(  
        'rest_framework.authentication.BasicAuthentication',  
        'rest_framework.authentication.SessionAuthentication',  
    )  
 }  

```

4. A  API  deve  ser  documentada  com  Swagger  ou  alguma  outra  sugestão  da página: 
http://www.django-rest-framework.org/topics/documenting-your-api/.

Neste projeto foi utilizado o Swagger, mas para utilizar foram necessárias algumas configurações no arquivo settings.py.
 Na variável ```INSTALLED_APPS``` foi adicionado a linha rest_framework_swagger.
Além disso, para detalhar ainda mais a documentação foi adicionado alguns comentários nas views no arquivo views.py, 
em que o Swagger entende como descrição dos verbos HTTP utilizados.
Como nem todas as entidades utitizam todos o verbos, foi necessário citar quais são das entidades na variável  
```http_method_names``` nas views. Como a figura abaixo, onde a entidade Sala só usam verbos get, head e options.

```python
class SalaDetail(generics.RetrieveAPIView):  
    ''''' 
    get: Mostra a sala especifica 
    '''  
    http_method_names = ['get','head','options']
```

A documentação está disponível na rota /swagger/. Isso porque foi definida no arquivo core/urls.py a url que depende da
 classe ```rest_framework_swagger.views.get_swagger_view```.
 

```python
 from rest_framework_swagger.views import get_swagger_view  
  
 schema_view = get_swagger_view(title='EdificioWebAPI')  
 urlpatterns = [  
 url(r'^swagger/$', schema_view),  
 ] 
 ```
5. Definir e usar critérios de paginação e Throttling. Esse último deve diferenciar usuários autenticados de não
 autenticados

Para criar paginação em todas as entidades basta adicionar na variável de configuração do DRF as classes
  ```rest_framework.pagination.LimitOffsetPagination ``` e depois informar o tamanho. Neste projeto ele está 
 configurado desta forma:
 

```python
 REST_FRAMEWORK = {  
             'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',  
    'PAGE_SIZE': 5  
 } 
 ```
 
 Nos critérios de Throttling, será restringidos para usuários não autenticados 10 requisições por hora, para usuários 
 autenticados 20 requisições por hora e para a entidade sala será permitido 5 restrições por dia. A variável de 
 configuração do DRF no arquivo settings.py deve ter as classes para limitar o uso da API, além das taxas máximas de
  requisições.
  
 Depois disso foi configurado as views da entidade especifica, a Sala, informando o nome específico definido anteriormente.


```python
from rest_framework.throttling import ScopedRateThrottle

class SalaList(generics.ListAPIView):
    throttle_scope = 'salas'
    throttle_classes = (ScopedRateThrottle,)
 ```
 
 
6. Implementar pelo menos 2 entidades: filtros, busca e ordenação

Considerando o tema do modelo deste projeto as opções escolhidas para implementar foram um busca e uma ordenação para 
as respectivas entidades  ```Cliente ``` e  ```ItemAgenda ```.
Na busca primeramente foi adicionada a classe  ```django_filters.rest_framework.DjangoFilterBackend ``` na variável de 
configuração do DRF no arquivo settings.py. Depois na view da classe escolhida para ter a busca, neste caso a view do 
 ```Cliente ```, foram adicionadas as seguintes variáveis:
 

```python
from django_filters.rest_framework import DjangoFilterBackend

class ClienteList(generics.ListCreateAPIView):
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome','cpf')

```

De acordo com isso, o cliente poderá ser pesquisado pelo nome ou cpf no botão que será adicionado na pagina da lista de
 clientes. 


![busca](/imagens/busca.png)

Para implementar a opção de ordenação dos itens da agenda, foi necessário configurar novamente o arquivo settings.py 
adicionando a aplicação ```django_filters``` na variavel ```INSTALLED_APPS```. Além disso foi adicionado nos atributos o que 
poderia ser ordenado nesta entidade. 



```python
from rest_framework.filters import OrderingFilter

class ItemAgendaList(generics.ListCreateAPIView):
   filter_backends = (OrderingFilter,)
   ordering_fields = ('data', 'horario')
```

Dessa forma, as instâncias de ```ItemAgenda``` podem ser ordenadas ascendentes ou descendentes pela data e pelo horário.
 
 
![ordenação](/imagens/ordenação.png)


7. Criar testes unitários e de cobertura

Os testes estão localizado no arquivo core.tests.py e para executa-los o comando é 
```python manage.py test core.tests```

Foram criados os principais testes para as entidades como de visualizar, criar, editar e apagar, considerando todas as 
permissões e usuários autenticados ou não.
    




