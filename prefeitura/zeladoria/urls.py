from django.urls import path
from . import views

urlpatterns = [
    path("", views.zeladoria),
    path("coleta_de_poda", views.coleta_de_poda),
    path("terreno_sem_conservacao", views.terreno_sem_conservacao),
    path("limpeza_de_proprios_municipais", views.limpeza_de_proprios_municipais),
    path("cata_treco", views.cata_treco),
    path("denuncia_de_descarte_irregular_de_residuos", views.denuncia_de_descarte_irregular_de_residuos),
    path("coleta_de_residuos_diversificados", views.coleta_de_residuos_diversificados),
    path("varricao_de_logradouros_publicos", views.varricao_de_logradouros_publicos),
    path("coleta_seletiva", views.coleta_seletiva),
    path("falha_na_coleta_domiciliar", views.falha_na_coleta_domiciliar),
    path("coleta_de_animais_mortos", views.coleta_de_animais_mortos),
    
]
