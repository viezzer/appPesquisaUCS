from datetime import datetime, date
from django.test import TestCase
from django.urls import reverse
from ..models import Projeto

class ProjetoCRUDTest(TestCase):
    def setUp(self):
        self.projeto = Projeto.objects.create(
            nome='Projeto de Mestrado em Biotecnologia',
            descricao='Um projeto de pesquisa...',
            situacao='encerrado',
            natureza='Pesquisa',
            criado_em=datetime.today().date(),
            data_encerramento=date(2024, 1, 1)  
        )

    def test_projeto_list(self):
        response = self.client.get(reverse('appPesquisa:projeto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.projeto.nome)

    def test_projeto_detail(self):
        response = self.client.get(reverse('appPesquisa:projeto_detail', args=[self.projeto.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.projeto.nome)

    def test_projeto_create(self):
        response = self.client.post(reverse('appPesquisa:projeto_create'), {
            'nome': 'MBA em Admnistração de empresas',
            'descricao': 'Projeto de análise sobre o setor...',
            'situacao': 'em andamento',
            'natureza': 'MBA',
            'criado_em': datetime.today().date(),
            'data_encerramento': date(2024, 1, 1)
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Projeto.objects.count(), 2)

    def test_projeto_update(self):
        response = self.client.post(reverse('appPesquisa:projeto_update', args=[self.projeto.pk]), {
            'nome': 'Nome alterado',
            'descricao': 'Projeto de análise sobre o setor...',
            'situacao': 'em andamento',
            'natureza': 'MBA',
            'criado_em': datetime.today().date(),
            'data_encerramento': date(2024, 1, 1)
        })
        self.assertEqual(response.status_code, 302)
        self.projeto.refresh_from_db()
        self.assertEqual(self.projeto.nome, 'Nome alterado')

    def test_projeto_delete(self):
        response = self.client.post(reverse('appPesquisa:projeto_delete', args=[self.projeto.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Projeto.objects.count(), 0)

class ProjetoListFilterTest(TestCase):
    def setUp(self):
        # Criando alguns projetos de exemplo
        Projeto.objects.create( 
            nome='Projeto 1',
            descricao='Descrição do projeto chamado 1',
            situacao='encerrado',
            natureza='Pesquisa',
            criado_em=datetime.today().date(),
            data_encerramento=date(2024, 1 ,1))
        
        Projeto.objects.create( 
            nome='Projeto de Mestrado em Biotecnologia',
            descricao='Um projeto de pesquisa...',
            situacao='em progresso',
            natureza='Pesquisa',
            criado_em=datetime.today().date(),
            data_encerramento=date(2024, 1 ,1))

        Projeto.objects.create( 
            nome='Projeto de Serviços',
            descricao='Um projeto...',
            situacao='prorrogado',
            natureza='Serviços',
            criado_em=datetime.today().date(),
            data_encerramento=date(2024, 1 ,1))

    def test_projeto_filtro_por_nome(self):
        # Realiza uma pesquisa por nome
        response = self.client.get(reverse('appPesquisa:projeto_list'), {'nome': 'Projeto 1'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa retornou apenas o projeto correto
        self.assertEqual(response.context['projetos'][0].nome, 'Projeto 1')
        self.assertEqual(response.context['projetos'][0].descricao, 'Descrição do projeto chamado 1')
        self.assertEqual(response.context['projetos'][0].situacao, 'encerrado')
        self.assertEqual(response.context['projetos'][0].natureza, 'Pesquisa')
        self.assertEqual(response.context['projetos'][0].criado_em, datetime.today().date())
        self.assertEqual(response.context['projetos'][0].data_encerramento, date(2024, 1 ,1))
        
    def test_projeto_filtro_por_nome_sem_resultados(self):
        # Realiza uma pesquisa por nome que não retorna resultados
        response = self.client.get(reverse('appPesquisa:projeto_list'), {'nome': 'Título de projeto que não existe'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa não retornou nenhum resultado
        self.assertEqual(len(response.context['projetos']), 0)


    def test_projeto_filtro_por_natureza(self):
        # Realiza uma pesquisa por nome
        response = self.client.get(reverse('appPesquisa:projeto_list'), {'natureza': 'Pesquisa'})

        # Verifica se a resposta é 200 (sucesso)
        self.assertEqual(response.status_code, 200)

        # Verifica se a pesquisa retornou apenas o projeto correto
        self.assertEqual(response.context['projetos'][0].nome, 'Projeto 1')
        self.assertEqual(response.context['projetos'][0].descricao, 'Descrição do projeto chamado 1')
        self.assertEqual(response.context['projetos'][0].situacao, 'encerrado')
        self.assertEqual(response.context['projetos'][0].natureza, 'Pesquisa')
        self.assertEqual(response.context['projetos'][0].criado_em, datetime.today().date())
        self.assertEqual(response.context['projetos'][0].data_encerramento, date(2024, 1 ,1))