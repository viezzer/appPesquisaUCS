from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Pesquisador

class PesquisadorListView(ListView):
    model = Pesquisador
    template_name = 'pesquisador/list.html'
    context_object_name = 'pesquisadores'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        tipo = self.request.GET.get('tipo')
        area_atuacao = self.request.GET.get('area_atuacao')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if tipo:
            queryset = queryset.filter(tipo__icontains=tipo)
        if area_atuacao:
            queryset = queryset.filter(area_atuacao__icontains=area_atuacao)

        return queryset

class PesquisadorCreateView(CreateView):
    model = Pesquisador
    template_name = 'pesquisador/create.html'
    fields = ['nome', 'tipo', 'area_atuacao']
    success_url = reverse_lazy('appPesquisa:pesquisador_list')

class PesquisadorUpdateView(UpdateView):
    model = Pesquisador
    template_name = 'pesquisador/update.html'
    fields = ['nome', 'tipo', 'area_atuacao']
    def get_success_url(self):
        return reverse_lazy('appPesquisa:pesquisador_detail', kwargs={'pesquisador_id': self.object.pk})

class PesquisadorDeleteView(DeleteView):
    model = Pesquisador
    template_name = 'pesquisador/delete.html'
    success_url = reverse_lazy('appPesquisa:pesquisador_list')

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

def pesquisadorDetail(request, pesquisador_id):
    pesquisador = get_object_or_404(Pesquisador,pk=pesquisador_id)
    return render(request, "pesquisador/detail.html", {"pesquisador": pesquisador})

def pesquisadorProjetos(request, pesquisador_id):
    response = "Você está procurando pelos projetos de %s."
    return HttpResponse(response % pesquisador_id)

def pesquisadorResultados(request, pesquisador_id):
    response = "Você está procurando pelos resultados de %s."
    return HttpResponse(response % pesquisador_id)

def index(request):
    return render(request, "index.html")