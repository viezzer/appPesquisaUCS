from django.db import models

class Pesquisador(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome