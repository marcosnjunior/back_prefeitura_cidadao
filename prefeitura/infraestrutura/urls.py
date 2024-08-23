from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("problema_iluminacao",views.problema_iluminacao),
    path("expansao_iluminacao",views.expansao_iluminacao),
    path("manutencaoVias",views.manutencao),
    path("manutencaoVias/tapa_buraco",views.tapa_buraco),
    path("manutencaoVias/galeria_boca_lobo",views.galeria_boca_lobo),
    path("manutencaoVias/terraplanagem",views.terraplanagem),
    path("manutencao_pracas",views.manutencao_pracas),
    path("manutencao_pracas/pinturas",views.pinturas),
    path("manutencao_pracas/hidraulicos",views.hidraulicos),
    path("manutencao_pracas/eletricos",views.eletricos),
    path("manutencao_pracas/serralharia",views.serralharia),
    path("manutencao_pracas/jardinagem",views.tapa_buraco),
    path("manutencao_pracas/marcenaria",views.marcenaria),
]