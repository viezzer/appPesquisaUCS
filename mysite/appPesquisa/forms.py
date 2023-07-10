from django import forms
from .models import Pesquisador, PesquisadorProjeto, Projeto, OPCOES_SITUACAO, Resultado


class PesquisadorForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    tipo = forms.ChoiceField(label='Tipo de pesquisador', widget=forms.Select(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    area_atuacao = forms.CharField(label='Área de atuação', widget=forms.Select(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    
    class Meta:
        model = Pesquisador
        fields = ['nome', 'tipo', 'area_atuacao']


class ProjetoPesquisadorForm(forms.ModelForm):
    OPCOES_PAPEL = (
        ('integrante', 'Integrante'),
        ('coordenador', 'Coordenador'),
    )
    pesquisador = forms.ModelChoiceField(
        queryset=Pesquisador.objects.all(),
        widget=forms.Select(attrs={'class': 'border border-gray-300 rounded px-4 py-2'})
    )
    papel = forms.ChoiceField(label='Papel', choices=PesquisadorProjeto.OPCOES_PAPEL ,
                              widget=forms.Select(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    date_joined = forms.DateField(label='Data de entrada', widget=forms.DateInput(
        format='%d.%m.%Y',attrs={'class': 'border border-gray-300 rounded px-4 py-2', 'type': 'date'}))
    class Meta:
        model = PesquisadorProjeto
        fields = ['pesquisador','papel', 'date_joined']


class ProjetoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(
        attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(
        attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    situacao = forms.ChoiceField(label='Situação', choices=OPCOES_SITUACAO ,widget=forms.Select(
        attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    natureza = forms.CharField(label='Natureza', max_length=100, widget=forms.TextInput(
        attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    criado_em = forms.DateField(label='Data de criação', widget=forms.DateInput(format='%d.%m.%Y',
        attrs={'class': 'border border-gray-300 rounded px-4 py-2', 'type': 'date'}))
    data_encerramento = forms.DateField(label='Data de encerramento', widget=forms.DateInput(format='%d.%m.%Y',
        attrs={'class': 'border border-gray-300 rounded px-4 py-2', 'type': 'date'}))
    
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'situacao', 'natureza', 'criado_em', 'data_encerramento']


class ResultadoForm(forms.ModelForm):
    OPCOES_TIPO = (
        ('artigo', 'Artigo'),
        ('servico', 'Serviço'),
        ('relatorio', 'Relatório'),
        ('produto', 'Produto'),
        ('prototipo', 'Protótipo')
    )
    tipo = forms.ChoiceField(label='Tipo de resultado', choices=OPCOES_TIPO, widget=forms.Select(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    titulo = forms.CharField(label='Título', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    
    class Meta:
        model = Resultado
        fields = ['tipo', 'titulo', 'descricao']
        