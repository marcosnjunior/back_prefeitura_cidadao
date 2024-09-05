from django.urls import path
from . import views

urlpatterns = [
    path("autorizacao_arborea",views.home),
    path("plantio_de_arvores",views.plantio),
    path("poda_de_arvores", views.poda),
    path("denuncia_ambiental", views.denuncia_ambiental),
    path("lancamento_de_agua_servidas", views.lancamento),
    path("lancamento_esgoto", views.esgoto),
    path("poluicao_sonora", views.poluicaoSonora),
    path("corte_irregular_arvores", views.corteIrregularArvores),
    path("poluicao_atmosferica", views.poluicaoAtmosferica),
    path("invasao_area_preservacao_permanente", views.invasaoAreaPreservacaoPermanente),
    path("admin_plantio", views.admin_plantio_arvores),
]