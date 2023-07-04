from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import ProjetoForm

from .models import PesquisadorProjeto, Projeto, Pesquisador, Resultado

class ProjetosListView(ListView):
    model = Projeto
    template_name = 'projeto/list.html'
    context_object_name = 'projetos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        situacao = self.request.GET.get('situacao')
        natureza = self.request.GET.get('natureza')
        criado_em = self.request.GET.get('criado_em')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if situacao:
            queryset = queryset.filter(situacao__icontains=situacao)
        if natureza:
            queryset = queryset.filter(natureza__icontains=natureza)
        if criado_em:
            queryset = queryset.filter(criado_em=criado_em)

        return queryset

class ProjetoCreateView(CreateView):
    model = Projeto
    template_name = 'projeto/create.html'
    form_class = ProjetoForm
    success_url = reverse_lazy('appPesquisa:projeto_list')

    #override the create object method
    # def form_valid(self, form):
    #     projeto = form.save()
    #     pesquisadores = form.cleaned_data['membros']
    #     for pesquisador in pesquisadores:
    #         PesquisadorProjeto.objects.create(pesquisador=pesquisador, projeto=projeto, papel='integrante')
    #     return super().form_valid(form)
    


class ProjetoUpdateView(UpdateView):
    model = Projeto
    template_name = 'projeto/update.html'
    form_class = ProjetoForm

    #field criado_em is not receiving the value from the object
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['criado_em'].initial = self.object.criado_em.strftime('%d.%m.%Y')
        return form

    
    def get_success_url(self):
        return reverse_lazy('appPesquisa:projeto_detail', kwargs={'projeto_id': self.object.pk})

class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = 'projeto/delete.html'
    success_url = reverse_lazy('appPesquisa:projeto_list')

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

def projetoDetail(request, projeto_id):
    projeto = get_object_or_404(Projeto,pk=projeto_id)
    relacao_pesquisadores = PesquisadorProjeto.objects.filter(projeto=projeto_id)
    resultados = Resultado.objects.filter(projeto=projeto_id)
    return render(request, "projeto/detail.html", {"projeto": projeto, "pesquisadores": relacao_pesquisadores, "resultados": resultados})

def pesquisadorProjetos(request, projeto_id):
    response = "Você está procurando pelos projetos de %s."
    return HttpResponse(response % projeto_id)

def projetoResultados(request, projeto_id):
    response = "Você está procurando pelos resultados de %s."
    return HttpResponse(response % projeto_id)