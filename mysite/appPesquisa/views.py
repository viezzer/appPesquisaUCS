from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse

from .models import Pesquisador
from .forms import PesquisadorForm


def index(request):
    raise Http404("Página em construçao")

def cadastrarPesquisador(request):
    if request.method == 'POST':
        form = PesquisadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appPesquisa:listarPesquisadores')
    else:
        form = PesquisadorForm()
    
    return render(request, 'pesquisador/cadastro.html', {'form': form})

def listarPesquisadores(request):
    pesquisadores = Pesquisador.objects.order_by("nome")
    # Verifica se há parâmetro de filtro na URL
    nome_filtro = request.GET.get('nome')
    if nome_filtro:
        pesquisadores = pesquisadores.filter(nome__iexact=nome_filtro)

    area_filtro = request.GET.get('area_atuacao')
    if area_filtro:
        pesquisadores = pesquisadores.filter(area_atuacao__iexact=area_filtro)
    
    # Renderiza o template com a lista de pesquisadores
    return render(request, 'pesquisador/index.html', {'pesquisadores': pesquisadores})

def pesquisadorDetail(request, pesquisador_id):
    pesquisador = get_object_or_404(Pesquisador,pk=pesquisador_id)
    return render(request, "pesquisador/detail.html", {"pesquisador": pesquisador})

def pesquisadorProjetos(request, pesquisador_id):
    response = "Você está procurando pelos projetos de %s."
    return HttpResponse(response % pesquisador_id)

def pesquisadorResultados(request, pesquisador_id):
    response = "Você está procurando pelos resultados de %s."
    return HttpResponse(response % pesquisador_id)