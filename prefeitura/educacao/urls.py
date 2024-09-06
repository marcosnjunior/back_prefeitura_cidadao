from django.urls import path
from . import views

urlpatterns = [
    path("", views.educacao),
    path("autorizacao_de_estagio_supervisionado", views.autorizacao_de_estagio_supervisionado),
    path("autorizacao_para_pesquisa_crei_escola", views.autorizacao_para_pesquisa_crei_escola),
    path("furto_extravio_ou_perda_de_equipamentos", views.furto_extravio_ou_perda_de_equipamentos),
    path("solicitacao_de_espaco_fisico_escola_crei", views.solicitacao_de_espaco_fisico_escola_crei),
    path("solicitacao_diversa", views.solicitacao_diversa),
    path("admin", views.admin),
    path("educacao_admin", views.admin),
]
