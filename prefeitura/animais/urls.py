from django.urls import path

from . import views

urlpatterns = [
    # base
    path('apreensao-de-animal', views.apreensao_base),
    path('saude-animal', views.saudeanimal_base),
    path('bem-estar-animal', views.bemestaranimal_base),
    # outros   
    path('apreensao-de-animal/coleta-animais-mortos/', views.coleta),
    path('apreensao-de-animal/apreensao-de-animais/', views.Apreensao),
    path('saude-animal/denuncia-de-animais', views.Denuncia),
    path('bem-estar-animal/agenda-consulta-clinica', views.AgendaConsulta),
    path('bem-estar-animal/agenda-castracao-pet', views.AgendaCastracao),
    path('bem-estar-animal/hospital-veterinario', views.HospitalVeterinario),
]