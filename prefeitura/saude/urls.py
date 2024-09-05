from django.urls import path
from . import views

urlpatterns = [
    path("vigilancia-sanitaria", views.vigilancia_sanitaria),
    path("admin/vigilancia-sanitaria", views.vigilancia_sanitaria_admin),
    path("vacina", views.vacina),
    path("opera-mais", views.opera_mais),
    path("remedio-em-casa", views.remedio_em_casa),
    path("cartao-sus", views.cartao_sus),
    path("lgbt-igualdade", views.lgbt_igualdade),
    path("vigilancia-sanitaria/denuncias", views.denuncias),
    # remedio-em-casa
    path("remedio-em-casa/pedidos-remedios", views.pedidos_remedios),
    path("remedio-em-casa/renovacao-receita", views.renovacao_receita),
    # opera-mais
    path("opera-mais/solicite-cirurgia", views.solicite_cirurgia),
    path("opera-mais/exames", views.solicete_exames),
    # vacina
    path("vacina/vacinacao-domiciliar", views.vacinacao),
    # LGBT
    path("lgbt-igualdade/consulta-ginecologista", views.consulta_ginecologista_lgbt),
    path("lgbt-igualdade/gastroenterologista", views.gastroenterologista),
    path("lgbt-igualdade/exame-citopatologico", views.exame_citopatologico),
    path("lgbt-igualdade/exame-endocrinologia", views.exame_endocrinologia),
    # cartaosus
    path("cartao-sus/solicite-cartao-sus", views.solicite_cartao_sus),
]