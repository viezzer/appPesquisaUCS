from django.db import models

class Pesquisador(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('funcionario', 'Funcionário'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    area_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    OPCOES_SITUACAO = (
        ('em andamento', 'Em andamento'),
        ('encerrado', 'Encerrado'),
    )
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    situacao = models.CharField(max_length=100, choices=OPCOES_SITUACAO)
    natureza = models.CharField(max_length=100)
    criado_em = models.DateTimeField()
    membros = models.ManyToManyField(Pesquisador, through="PesquisadorProjeto")

    def __str__(self):
        return self.nome

class PesquisadorProjeto(models.Model):
    OPCOES_PAPEL = (
        ('integrante', 'Integrante'),
        ('coordenador', 'Coordenador'),
    )
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    papel = models.CharField(max_length=64, choices=OPCOES_PAPEL)
    date_joined = models.DateField()