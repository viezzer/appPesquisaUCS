from django import forms
from .models import Pesquisador

class PesquisadorForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    tipo = forms.CharField(label='Tipo de pesquisador', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    area_atuacao = forms.CharField(label='Área de atuação', max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-4 py-2'}))
    
    class Meta:
        model = Pesquisador
        fields = ['nome', 'tipo', 'area_atuacao']
        