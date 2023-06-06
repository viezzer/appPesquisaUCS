from django.test import TestCase
from django.urls import reverse
from .models import Pesquisador

class PesquisadorCRUDTest(TestCase):
    def setUp(self):
        self.pesquisador = Pesquisador.objects.create(
            nome='John Doe',
            tipo='aluno',
            area_atuacao='Ciência da Computação'
        )

    def test_pesquisador_list(self):
        response = self.client.get(reverse('appPesquisa:pesquisador_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pesquisador.nome)

    def test_pesquisador_detail(self):
        response = self.client.get(reverse('appPesquisa:pesquisador_detail', args=[self.pesquisador.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pesquisador.nome)

    def test_pesquisador_create(self):
        response = self.client.post(reverse('appPesquisa:pesquisador_create'), {
            'nome': 'Jane Smith',
            'tipo': 'professor',
            'area_atuacao': 'Matemática'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pesquisador.objects.count(), 2)

    def test_pesquisador_update(self):
        response = self.client.post(reverse('appPesquisa:pesquisador_update', args=[self.pesquisador.pk]), {
            'nome': 'Updated Name',
            'tipo': 'funcionario',
            'area_atuacao': 'Engenharia'
        })
        self.assertEqual(response.status_code, 302)
        self.pesquisador.refresh_from_db()
        self.assertEqual(self.pesquisador.nome, 'Updated Name')

    def test_pesquisador_delete(self):
        response = self.client.post(reverse('appPesquisa:pesquisador_delete', args=[self.pesquisador.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pesquisador.objects.count(), 0)

class PesquisadorListFilterTest(TestCase):
    def setUp(self):
        # Criando alguns pesquisadores de exemplo
        Pesquisador.objects.create(nome='João', tipo='aluno', area_atuacao='Biologia')
        Pesquisador.objects.create(nome='Maria', tipo='professor',  area_atuacao='Química')
        Pesquisador.objects.create(nome='Pedro', tipo='funcionario',  area_atuacao='Física')

    def test_pesquisador_filtro_por_nome(self):
        # Realiza uma pesquisa por nome
        response = self.client.get(reverse('appPesquisa:pesquisador_list'), {'nome': 'João'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa retornou apenas o pesquisador correto
        self.assertEqual(len(response.context['pesquisadores']), 1)
        self.assertEqual(response.context['pesquisadores'][0].nome, 'João')
        self.assertEqual(response.context['pesquisadores'][0].tipo, 'aluno')
        self.assertEqual(response.context['pesquisadores'][0].area_atuacao, 'Biologia')

    def test_pesquisador_filtro_por_area_atuacao(self):
        # Realiza uma pesquisa por nome
        response = self.client.get(reverse('appPesquisa:pesquisador_list'), {'area_atuacao': 'Biologia'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa retornou apenas o pesquisador correto
        self.assertEqual(len(response.context['pesquisadores']), 1)
        self.assertEqual(response.context['pesquisadores'][0].nome, 'João')
        self.assertEqual(response.context['pesquisadores'][0].tipo, 'aluno')
        self.assertEqual(response.context['pesquisadores'][0].area_atuacao, 'Biologia')

    def test_pesquisador_filtro_por_nome_sem_resultados(self):
        # Realiza uma pesquisa por nome que não retorna resultados
        response = self.client.get(reverse('appPesquisa:pesquisador_list'), {'nome': 'Carlos'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa não retornou nenhum resultado
        self.assertEqual(len(response.context['pesquisadores']), 0)

    def test_pesquisador_filtro_por_area_atuacao_sem_resultados(self):
        # Realiza uma pesquisa por nome que não retorna resultados
        response = self.client.get(reverse('appPesquisa:pesquisador_list'), {'area_atuacao': 'Criminal'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa não retornou nenhum resultado
        self.assertEqual(len(response.context['pesquisadores']), 0)
