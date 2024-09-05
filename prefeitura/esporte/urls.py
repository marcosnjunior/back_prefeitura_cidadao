from django.urls import path
from . import views



urlpatterns = [
    path("", views.esporte),
    path("Recebimento_de_convites", views.recebimento_de_Convites),
    path("solicitacao_de_apoio", views.solicitacao_de_Apoio),
    path("solicitacao_de_material", views.solicitacao_de_Material),
    path("solicitacao_de_reparos_e_manutencao_de_equipamentos", views.solicitacao_de_Reparos_e_Manutencao_de_Equipamentos),
    path("solicitacao_de_uso_de_espaco_fisico", views.solicitacao_de_Uso_de_Espaco_Fisico),
    path("esporte_admin", views.esporte_admin),
    
]