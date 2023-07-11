from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ResultadoForm


from .models import Projeto, Resultado

class ResultadoCreateView(CreateView):
    model = Resultado
    template_name = 'resultado/create.html'
    form_class = ResultadoForm
    success_url = reverse_lazy('appPesquisa:projeto_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projeto_id = self.kwargs['projeto_id']
        projeto = get_object_or_404(Projeto, pk=projeto_id)
        context['projeto'] = projeto
        return context

    # add the project to the object before saving
    def form_valid(self, form):
        form.instance.projeto = get_object_or_404(Projeto, pk=self.kwargs['projeto_id'])
        return super().form_valid(form)
    

class ResultadoUpdateView(UpdateView):
    model = Resultado
    template_name = 'resultado/update.html'
    form_class = ResultadoForm
    success_url = reverse_lazy('appPesquisa:projeto_list')

    def get_object(self):
        return get_object_or_404(Resultado, pk=self.kwargs['resultado_id'])
    
    #add the data on the form
    def get_initial(self):
        initial = super().get_initial()
        initial['projeto'] = self.object.projeto
        return initial
    

class ResultadoDeleteView(DeleteView):
    model = Resultado
    template_name = 'resultado/delete.html'
    success_url = reverse_lazy('appPesquisa:projeto_list')

    def get_object(self):
        return get_object_or_404(Resultado, pk=self.kwargs['resultado_id'])
    
    

#create a detail view for the resultado
def resultadoDetail(request, resultado_id):
    resultado = get_object_or_404(Resultado, pk=resultado_id)
    return render(request, 'resultado/detail.html', {'resultado': resultado})
