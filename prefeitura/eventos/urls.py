from django.contrib import admin
from django.urls import path
from . import views
#familia = familia_acolhedora
urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('familia_acolhedora', views.familia_acolhedora, name='familia_acolhedora'),



]