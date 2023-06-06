from django.urls import path

from . import views
from .views import PesquisadorListView, PesquisadorCreateView, PesquisadorUpdateView, PesquisadorDeleteView

app_name = 'appPesquisa'
urlpatterns = [
    path('pesquisadores/', PesquisadorListView.as_view(), name='pesquisador_list'),
    path('pesquisadores/create/', PesquisadorCreateView.as_view(), name='pesquisador_create'),
    path('pesquisadores/<int:pk>/', PesquisadorUpdateView.as_view(), name='pesquisador_update'),
    path('pesquisadores/<int:pk>/delete/', PesquisadorDeleteView.as_view(), name='pesquisador_delete'),
    # ex: /appPesquisa/
    path("", views.index, name="index"),
    # ex: /appPesquisa/pesquisador
    path("pesquisador/novo/", views.cadastrarPesquisador, name="cadastrarPesquisador"),
    # ex: /appPesquisa/pesquisador/
    path("pesquisador/", views.listarPesquisadores, name="listarPesquisadores"),
    # ex: /appPesquisa/pesquisador/5/
    path("pesquisador/<int:pesquisador_id>/", views.pesquisadorDetail, name="pesquisadorDetail"),
    # ex: /appPesquisa/pesquisador/5/projetos/
    path("pesquisador/<int:pesquisador_id>/projetos/", views.pesquisadorProjetos, name="pesquisadorProjetos"),
    # ex: /appPesquisa/pesquisador/5/resultados/
    path("pesquisador/<int:pesquisador_id>/resultados/", views.pesquisadorResultados, name="pesquisadorResultados"),
]