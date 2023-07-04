from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ResultadoForm


from .models import Projeto, Resultado

class ProjetoCreateView(CreateView):
    model = Resultado
    template_name = 'resultado/create.html'
    form_class = ResultadoForm
    success_url = reverse_lazy('appPesquisa:projeto_list')

    # add the project to the object before saving
    def form_valid(self, form):
        form.instance.projeto = get_object_or_404(Projeto, pk=self.kwargs['projeto_id'])
        return super().form_valid(form)
