from django.urls import path
from . import views

urlpatterns = [
    path("autorizacao_arborea",views.home),
    path("plantio_de_arvores",views.plantio),
    path("poda_de_arvores", views.poda),
    path("denuncia_ambiental", views.denuncia_ambiental),
    path("lancamento_de_agua_servidas", views.lancamento)
    
]