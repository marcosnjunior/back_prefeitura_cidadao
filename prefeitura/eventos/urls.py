from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.eventos, name='eventos'),
    path('', views.eventos),
    path('cultura', views.cultura, name='cultura'),
    path('cultura_', views.cultura_, name='cultura_'),
    path('conselho_tutelar', views.conselho_tutelar, name='conselho_tutelar'),
    path('conselho_tutelar_', views.conselho_tutelar_, name='conselho_tutelar_'),
    path('ptts_ouvidoria_maria_de_nazare', views.ptts_ouvidoria_maria_de_nazare, name='ptts_ouvidoria_maria_de_nazare'),
    path('maria_de_nazare', views.maria_de_nazare, name='maria_de_nazare'),
    path('familia_acolhedora', views.familia_acolhedora, name='familia_acolhedora'),
    path('familia_acolhedora_', views.familia_acolhedora_, name='familia_acolhedora_'),
    








]