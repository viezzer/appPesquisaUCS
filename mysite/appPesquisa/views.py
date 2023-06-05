from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import Http404
from django.http import HttpResponse

from .models import Pesquisador


def index(request):
    raise Http404("Página em construçao")

# def pesquisadorFormCadastro(request):
#     return render(request, "pesquisador/detail.html", {"pesquisador": pesquisador})

def listarPesquisadores(request):
    pesquisadores = Pesquisador.objects.order_by("nome")
    # Verifica se há parâmetro de filtro na URL
    nome_filtro = request.GET.get('nome')
    if nome_filtro:
        pesquisadores = pesquisadores.filter(nome__icontains=nome_filtro)

    area_filtro = request.GET.get('area_atuacao')
    if area_filtro:
        pesquisadores = pesquisadores.filter(area_atuacao__icontains=area_filtro)
    
    # Renderiza o template com a lista de pesquisadores
    return render(request, 'pesquisador/index.html', {'pesquisadores': pesquisadores})

def listarPesquisadoresFiltrados(request, nome):
    pesquisadores = Pesquisador.objects.filter(nome__icontains=nome)
    pesquisadores_filtrados = get_list_or_404(pesquisadores)
    context = {
        "pesquisadores": pesquisadores_filtrados,
    }
    return render(request, "pesquisador/index.html", context)

def pesquisadorDetail(request, pesquisador_id):
    pesquisador = get_object_or_404(Pesquisador,pk=pesquisador_id)
    return render(request, "pesquisador/detail.html", {"pesquisador": pesquisador})

def pesquisadorProjetos(request, pesquisador_id):
    response = "Você está procurando pelos projetos de %s."
    return HttpResponse(response % pesquisador_id)

def pesquisadorResultados(request, pesquisador_id):
    response = "Você está procurando pelos resultados de %s."
    return HttpResponse(response % pesquisador_id)