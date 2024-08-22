from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("problema_iluminacao",views.problema_iluminacao),
    path("expansao_iluminacao",views.expansao_iluminacao),
    path("manutencaoVias",views.manutencao),
    path("manutencaoVias/tapa_buraco",views.tapa_buraco),
    path("manutencaoVias/galeria_boca_lobo",views.tapa_buraco),
    path("manutencaoVias/terraplanagem",views.tapa_buraco),
]