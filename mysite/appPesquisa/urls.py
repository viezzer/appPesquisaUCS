from django.urls import path

from . import views

app_name = 'appPesquisa'
urlpatterns = [
    # ex: /appPesquisa/
    path("", views.index, name="index"),
    # ex: /appPesquisa/pesquisadores/
    path("pesquisador/", views.listarPesquisadores, name="listarPesquisadores"),
    # ex: /appPesquisa/5/
    path("pesquisador/<int:pesquisador_id>/", views.pesquisadorDetail, name="pesquisadorDetail"),
    # ex: /appPesquisa/5/pesquisadorprojetos/
    path("pesquisador/<int:pesquisador_id>/projetos/", views.pesquisadorProjetos, name="pesquisadorProjetos"),
    # ex: /appPesquisa/5/pesquisadorresultados/
    path("pesquisador/<int:pesquisador_id>/resultados/", views.pesquisadorResultados, name="pesquisadorResultados"),
]