from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.eventos, name='eventos'),
    path('', views.eventos),

    path('cultura', views.cultura, name='cultura'),
    path('cultura_', views.cultura_, name='cultura_'),
    path('funjope_Apoio_a_eventos_artisticos', views.funjope_Apoio_a_eventos_artisticos, name='funjope_Apoio_a_eventos_artisticos'),

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
    path('familia_acolhedora_', views.familia_acolhedora_, name='familia_acolhedora_'),
    








]