from django.urls import path
from . import views

urlpatterns = [
    # path("", views., name=""),
    path("defesa-civil/", views.defesa_civil, name="defesa_civil"),
    path("palestras-para-instituicoes-de-ensino", views.palestra, name="palestra"),
    path("registro-de-ocorrencia-e-desastre", views.registro, name="registro"),
    path("solicitacao-de-vistorias-preventivas", views.vistoria, name="vistoria"),
    path("alagamento", views.alagamento, name="alagamento"),
    path("desmoronamento", views.desmoronamento, name="desmoronamento"),

    path("guarda-municipal/", views.guarda_municipal, name="guarda_municipal"),
    path("secretaria-de-seguranca-urbana-cidadania", views.secretaria_de_seguranca_urbana_cidadania, name="secretaria_de_seguranca_urbana_cidadania"),
    path("solicitacao-de-guarnicao-para-evento", views.solicitacao_de_guarnicao, name="solicitacao_de_guarnicao"),
    path("solicitacao-de-rondas-da-guarda-municipal", views.solicitacao_de_rondas, name="solicitacao_de_rondas"),
    path("ligue-para-nos", views.ligue_para_nos, name="ligue_para_nos"),
    path("teatro-de-fantoches", views.teatro_de_fantoches, name="teatro_de_fantoches"),
    path("ouvidoria", views.ouvidoria, name="ouvidoria"),
    path("denuncie-aqui", views.denuncie_aqui, name="denuncie_aqui"),
]