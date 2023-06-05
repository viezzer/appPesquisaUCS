from django.test import TestCase
from django.urls import reverse
from .models import Pesquisador


class PesquisadorSearchTest(TestCase):
    def setUp(self):
        # Criando alguns pesquisadores de exemplo
        Pesquisador.objects.create(nome='João', tipo='aluno', area_atuacao='Biologia')
        Pesquisador.objects.create(nome='Maria', tipo='professor',  area_atuacao='Química')
        Pesquisador.objects.create(nome='Pedro', tipo='funcionario',  area_atuacao='Física')

    def test_pesquisador_filtro_por_nome(self):
        # Realiza uma pesquisa por nome
        response = self.client.get(reverse('appPesquisa:listarPesquisadores'), {'nome': 'João'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa retornou apenas o pesquisador correto
        self.assertEqual(len(response.context['pesquisadores']), 1)
        self.assertEqual(response.context['pesquisadores'][0].nome, 'João')
        self.assertEqual(response.context['pesquisadores'][0].tipo, 'aluno')
        self.assertEqual(response.context['pesquisadores'][0].area_atuacao, 'Biologia')

    def test_pesquisador_filtro_por_area_atuacao(self):
        # Realiza uma pesquisa por nome
        response = self.client.get(reverse('appPesquisa:listarPesquisadores'), {'area_atuacao': 'Biologia'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa retornou apenas o pesquisador correto
        self.assertEqual(len(response.context['pesquisadores']), 1)
        self.assertEqual(response.context['pesquisadores'][0].nome, 'João')
        self.assertEqual(response.context['pesquisadores'][0].tipo, 'aluno')
        self.assertEqual(response.context['pesquisadores'][0].area_atuacao, 'Biologia')

    def test_pesquisador_filtro_por_nome_sem_resultados(self):
        # Realiza uma pesquisa por nome que não retorna resultados
        response = self.client.get(reverse('appPesquisa:listarPesquisadores'), {'nome': 'Carlos'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa não retornou nenhum resultado
        self.assertEqual(len(response.context['pesquisadores']), 0)

    def test_pesquisador_filtro_por_area_atuacao_sem_resultados(self):
        # Realiza uma pesquisa por nome que não retorna resultados
        response = self.client.get(reverse('appPesquisa:listarPesquisadores'), {'area_atuacao': 'Criminal'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa não retornou nenhum resultado
        self.assertEqual(len(response.context['pesquisadores']), 0)
