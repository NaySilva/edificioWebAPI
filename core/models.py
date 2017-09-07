from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return 'Cliente %s' % (self.nome)


class Escritorio(models.Model):
    nome_escritorio = models.CharField(max_length=120)
    servico = models.CharField(max_length=120)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.nome_escritorio



class Sala(models.Model):
    numero = models.CharField(max_length=3)
    andar = models.CharField(max_length=2)
    escritorio = models.ForeignKey(Escritorio, on_delete=models.CASCADE, related_name='salas', null=True)
    descricao = models.CharField(max_length=120)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.descricao = self.descrever()

    def descrever(self):
        return 'Sala %s - %s Andar' % (self.numero, self.andar)

    def __str__(self):
        return 'Sala %s - %s Andar' % (self.numero, self.andar)

class Profissional(models.Model):
    user = models.ForeignKey('auth.User',default='1')
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=10)
    profissao = models.CharField(max_length=120)
    escritorio = models.ForeignKey(Escritorio, on_delete=models.CASCADE, related_name="profissionais", null=True)
    gerente = models.BooleanField(default=False)
    STATUS = (
        ('A', 'Ausente'),
        ('D', 'Disponível'),
        ('O', 'Ocupado'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default='A')

    def nomear(self):
        return self.user.username


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nome = self.nomear()

    def __str__(self):
        return 'Profissional %s' % (self.nome)



class ItemAgenda(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='agenda_profissional')
    horario = models.TimeField()
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agenda_cliente')
    escritorio = models.ForeignKey(Escritorio, on_delete=models.CASCADE, related_name='agenda_escritorio')
    SITUACAO = (
        ('A','Agendado'),
        ('R','Realizado'),
        ('C','Cancelado'),
        ('E','Em Andamento'),
    )
    situacao = models.CharField(max_length=1, choices=SITUACAO, default='A')

    class Meta:
        ordering = ('data', 'horario',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.escritorio = self.profissional.escritorio

    def __str__(self):
        return '%s - %s' % (self.cliente, self.profissional)
