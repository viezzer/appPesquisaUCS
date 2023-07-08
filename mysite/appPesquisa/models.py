import datetime
from django.db import models

OPCOES_SITUACAO = (
        ('em andamento', 'Em andamento'),
        ('encerrado', 'Encerrado'),
    )

class Pesquisador(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('funcionario', 'Funcionário'),
    ]
    
    ATUACAO_CHOICES = [
        ('Linguística, Letras e Artes', 'Linguística, Letras e Artes'),
        ('Ciências Humanas', 'Ciências Humanas'),
        ('Ciências Sociais Aplicadas', 'Ciências Sociais Aplicadas'),
        ('Ciências Agrárias', 'Ciências Agrárias'),
        ('Ciências da Saúde', 'Ciências da Saúde'),
        ('Engenharias', 'Engenharias'),
        ('Ciências Biológicas', 'Ciências Biológicas'),
        ('Ciências Exatas e da Terra', 'Ciências Exatas e da Terra'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    area_atuacao = models.CharField(max_length=100, choices=ATUACAO_CHOICES)

    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    situacao = models.CharField(max_length=100, choices=OPCOES_SITUACAO)
    natureza = models.CharField(max_length=100)
    criado_em = models.DateField(default=datetime.date.today)
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
    papel = models.CharField(max_length=64, choices=OPCOES_PAPEL, default='integrante')
    date_joined = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.pesquisador.nome + ' - ' + 'Papel: ' + self.papel
    

class Resultado (models.Model):
    OPCOES_TIPO = (
        ('artigo', 'Artigo'),
        ('servico', 'Serviço'),
        ('relatorio', 'Relatório'),
        ('produto', 'Produto'),
        ('prototipo', 'Protótipo')
    )
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=64, choices=OPCOES_TIPO, default='artigo')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo + ' - ' + self.tipo