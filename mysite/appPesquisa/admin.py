from django.contrib import admin

from .models import Pesquisador, Projeto, PesquisadorProjeto

admin.site.register(Pesquisador)
admin.site.register(Projeto)
admin.site.register(PesquisadorProjeto)
