from django.urls import path

from . import views

app_name = 'appPesquisa'
urlpatterns = [
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