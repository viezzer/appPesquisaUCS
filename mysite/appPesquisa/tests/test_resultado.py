from django.test import TestCase
from django.urls import reverse
from datetime import datetime, date
from ..models import Resultado, Projeto

class ResultadoCRUDTestCase(TestCase):
    def setUp(self):
        self.projeto = Projeto.objects.create(
            nome='Projeto de Mestrado em Biotecnologia',
            descricao='Um projeto de pesquisa...',
            situacao='andamento',
            natureza='Pesquisa',
            criado_em=datetime.today().date(),
            data_encerramento=date(2024, 1, 1)  
        )
        self.resultado = Resultado.objects.create(
            projeto=self.projeto,
            tipo='artigo',
            titulo='Título do Resultado',
            descricao='Descrição do Resultado'
        )

    def test_create_resultado(self):
        response = self.client.post(reverse('appPesquisa:resultado_create', kwargs={'projeto_id': self.projeto.id}), {
            'projeto': self.projeto.id,
            'tipo': 'servico',
            'titulo': 'Novo Resultado',
            'descricao': 'Descrição do Novo Resultado'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Resultado.objects.count(), 2)

    def test_read_resultado(self):
        response = self.client.get(reverse('appPesquisa:resultado_detail', kwargs={'resultado_id': self.resultado.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.resultado.titulo)
        self.assertContains(response, self.resultado.descricao)

    def test_update_resultado(self):
        response = self.client.post(reverse('appPesquisa:resultado_update', kwargs={'resultado_id': self.resultado.id}), {
            'projeto': self.projeto.id,
            'tipo': 'relatorio',
            'titulo': 'Novo Título',
            'descricao': 'Nova Descrição'
        })

        self.assertEqual(response.status_code, 302)
        self.resultado.refresh_from_db()
        self.assertEqual(self.resultado.tipo, 'relatorio')
        self.assertEqual(self.resultado.titulo, 'Novo Título')
        self.assertEqual(self.resultado.descricao, 'Nova Descrição')

    def test_delete_resultado(self):
        response = self.client.post(reverse('appPesquisa:resultado_delete', kwargs={'resultado_id': self.resultado.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Resultado.objects.count(), 0)
