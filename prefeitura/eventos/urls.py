from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.eventos, name='eventos'),
    path('', views.eventos),

    path('cultura', views.cultura, name='cultura'),
    path('funjope_Apoio_a_eventos_artisticos', views.funjope_Apoio_a_eventos_artisticos, name='funjope_Apoio_a_eventos_artisticos'),
    path('funjope_atestado_da_condicao_de_artista_local', views.funjope_atestado_da_condicao_de_artista_local, name='funjope_atestado_da_condicao_de_artista_local'),
    path('funjope_cadastramento_de_artistas_e_outros', views.funjope_cadastramento_de_artistas_e_outros, name='funjope_cadastramento_de_artistas_e_outros'),
    path('funjope_concertos_de_orquestra_sinfonica', views.funjope_concertos_de_orquestra_sinfonica, name='funjope_concertos_de_orquestra_sinfonica'),
    path('funjope_exposicao_de_artes_visuais', views.funjope_exposicao_de_artes_visuais, name='funjope_exposicao_de_artes_visuais'),
    path('funjope_edital_de_ocupacao_do_casa_da_polvora', views.funjope_edital_de_ocupacao_do_casa_da_polvora, name='funjope_edital_de_ocupacao_do_casa_da_polvora'),
    path('funjope_edital_de_ocupacao_do_casarao_34', views.funjope_edital_de_ocupacao_do_casarao_34, name='funjope_edital_de_ocupacao_do_casarao_34'),
    path('funjope_edital_de_ocupacao_do_hotel_globo', views.funjope_edital_de_ocupacao_do_hotel_globo, name='funjope_edital_de_ocupacao_do_hotel_globo'),
    path('funjope_instalacao_de_obras_de_arte', views.funjope_instalacao_de_obras_de_arte, name='funjope_instalacao_de_obras_de_arte'),
    path('funjope_jp_cultura', views.funjope_jp_cultura, name='funjope_jp_cultura'),
    path('funjope_jp_film_commission', views.funjope_jp_film_commission, name='funjope_jp_film_commission'),
    path('funjope_lei_dos_edificios', views.funjope_lei_dos_edificios, name='funjope_lei_dos_edificios'),
    path('funjope_prestacao_de_contas', views.funjope_prestacao_de_contas, name='funjope_prestacao_de_contas'),
    path('funjope_projeto_acao_social_pela_musica', views.funjope_projeto_acao_social_pela_musica, name='funjope_projeto_acao_social_pela_musica'),
    path('funjope_solicitacao_de_pagamento', views.funjope_solicitacao_de_pagamento, name='funjope_solicitacao_de_pagamento'),
    path('premio_joao_balula', views.premio_joao_balula, name='premio_joao_balula'),
    path('edital_de_formento', views.edital_de_formento, name='edital_de_formento'),
   
    path('conselho_tutelar', views.conselho_tutelar, name='conselho_tutelar'),
    path('conselho_tutelar_cristo', views.conselho_tutelar_cristo, name='conselho_tutelar_cristo'),
    path('conselho_tutelar_mangabeira', views.conselho_tutelar_mangabeira, name='conselho_tutelar_mangabeira'),
    path('conselho_tutelar_norte', views.conselho_tutelar_norte, name='conselho_tutelar_norte'),
    path('conselho_tutelar_praia', views.conselho_tutelar_praia, name='conselho_tutelar_praia'),
    path('conselho_tutelar_sudeste', views.conselho_tutelar_sudeste, name='conselho_tutelar_sudeste'),
    path('conselho_tutelar_sul', views.conselho_tutelar_sul, name='conselho_tutelar_sul'),
    path('conselho_tutelar_valentina', views.conselho_tutelar_valentina, name='conselho_tutelar_valentina'),
    path('conselho_tutelar_denuncia', views.conselho_tutelar_denuncia, name='conselho_tutelar_denuncia'),

    path('ptts_ouvidoria_maria_de_nazare', views.ptts_ouvidoria_maria_de_nazare, name='ptts_ouvidoria_maria_de_nazare'),
    path('maria_de_nazare', views.maria_de_nazare, name='maria_de_nazare'),

    path('familia_acolhedora', views.familia_acolhedora, name='familia_acolhedora'),
    path('familia_acolhedora_forms', views.familia_acolhedora_forms, name='familia_acolhedora_forms'),
    








]