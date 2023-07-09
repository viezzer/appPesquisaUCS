from django.urls import path

from . import views
from . import projetos_views
from . import resultados_view
from .views import PesquisadorListView, PesquisadorCreateView, PesquisadorUpdateView, PesquisadorDeleteView

app_name = 'appPesquisa'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('pesquisadores/', PesquisadorListView.as_view(), name='pesquisador_list'),
    path('pesquisadores/create/', PesquisadorCreateView.as_view(), name='pesquisador_create'),
    path('pesquisadores/<int:pk>/', PesquisadorUpdateView.as_view(), name='pesquisador_update'),
    path('pesquisadores/<int:pk>/delete/', PesquisadorDeleteView.as_view(), name='pesquisador_delete'),
    path("pesquisador/<int:pesquisador_id>/", views.pesquisadorDetail, name="pesquisador_detail"),

    path('projetos/', projetos_views.ProjetosListView.as_view(), name='projeto_list'),
    path('projetos/create/', projetos_views.ProjetoCreateView.as_view(), name='projeto_create'),
    path('projetos/<int:pk>/', projetos_views.ProjetoUpdateView.as_view(), name='projeto_update'),
    path('projetos/<int:pk>/delete/', projetos_views.ProjetoDeleteView.as_view(), name='projeto_delete'),
    path("projeto/<int:projeto_id>/", projetos_views.projetoDetail, name="projeto_detail"),

    path('projetos/resultados/<int:projeto_id>', resultados_view.ResultadoCreateView.as_view(), name='resultado_create'),
    path('projetos/resultados/<int:resultado_id>/update', resultados_view.ResultadoUpdateView.as_view(), name='resultado_update'),
    path('projetos/resultados/<int:resultado_id>/delete', resultados_view.ResultadoDeleteView.as_view(), name='resultado_delete'),
    path("projetos/resultados/<int:resultado_id>/", resultados_view.resultadoDetail, name="resultado_detail"),

]