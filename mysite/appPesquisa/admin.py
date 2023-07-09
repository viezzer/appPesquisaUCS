from django.contrib import admin

from .models import Pesquisador, Projeto, PesquisadorProjeto, Resultado

admin.site.register(Pesquisador)
admin.site.register(Projeto)
admin.site.register(PesquisadorProjeto)
admin.site.register(Resultado)
