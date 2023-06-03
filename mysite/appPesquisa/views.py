from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Pesquisador


def index(request):
    pesquisadores = Pesquisador.objects.order_by("nome")
    context = {
        "pesquisadores": pesquisadores,
    }
    return render(request, "pesquisador/index.html", context)

def listarPesquisadores(request):
    return HttpResponse("Você está procurando uma lista de pesquisadores")

def pesquisadorDetail(request, pesquisador_id):
    return HttpResponse("Você está procurando por %s." % pesquisador_id)

def pesquisadorProjetos(request, pesquisador_id):
    response = "Você está procurando pelos projetos de %s."
    return HttpResponse(response % pesquisador_id)

def pesquisadorResultados(request, pesquisador_id):
    response = "Você está procurando pelos resultados de %s."
    return HttpResponse(response % pesquisador_id)