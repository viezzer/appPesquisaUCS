from django import forms
from .models import Pesquisador, Projeto, OPCOES_SITUACAO

class PesquisadorForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    tipo = forms.ChoiceField(label='Tipo de pesquisador', widget=forms.Select(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    area_atuacao = forms.CharField(label='Área de atuação', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    
    class Meta:
        model = Pesquisador
        fields = ['nome', 'tipo', 'area_atuacao']


class ProjetoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    situacao = forms.ChoiceField(label='Situação', choices=OPCOES_SITUACAO ,widget=forms.Select(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    natureza = forms.CharField(label='Natureza', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    criado_em = forms.DateField(label='Data de criação', widget=forms.DateInput(format='%d.%m.%Y',attrs={'class': 'border border-gray-300 rounded px-4 py-2', 'type': 'date'}))
    membros = forms.ModelMultipleChoiceField(
        queryset=Pesquisador.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'situacao', 'natureza', 'criado_em', 'membros']
