from django.urls import path

from . import views

urlpatterns = [
    path('coleta-animais-mortos', views.coleta),
    path('apreensao-de-animais', views.Apreensao),
    path('denuncia-de-animais', views.Denuncia),
]