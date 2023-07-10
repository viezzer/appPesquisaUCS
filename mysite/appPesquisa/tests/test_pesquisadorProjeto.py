from django.test import TestCase
from ..models import Pesquisador, Projeto, PesquisadorProjeto

class PesquisadorProjetoTestCase(TestCase):
    def setUp(self):
        self.pesquisador = Pesquisador.objects.create(
            nome='John Doe',
            tipo='aluno',
            area_atuacao='Ciências Exatas e da Terra'
        )
        self.projeto = Projeto.objects.create(
            nome='Projeto Teste',
            descricao='Descrição do projeto teste',
            situacao='em andamento',
            natureza='natureza do projeto',
            criado_em='2023-01-01',
            data_encerramento='2023-12-31'
        )
        self.pesquisador_projeto = PesquisadorProjeto.objects.create(
            pesquisador=self.pesquisador,
            projeto=self.projeto,
            papel='integrante',
            date_joined='2023-01-01'
        )

    def test_pesquisador_projeto_str(self):
        self.assertEqual(str(self.pesquisador_projeto), 'John Doe - Papel: integrante')

    def test_pesquisador_projeto_dados_relacionamento_para_string(self):
        expected_result = 'Projeto: Projeto Teste - Papel: integrante'
        self.assertEqual(self.pesquisador_projeto.dados_relacionamento_para_string(), expected_result)

    def test_pesquisador_projeto_pesquisador(self):
        self.assertEqual(self.pesquisador_projeto.pesquisador, self.pesquisador)

    def test_pesquisador_projeto_projeto(self):
        self.assertEqual(self.pesquisador_projeto.projeto, self.projeto)
