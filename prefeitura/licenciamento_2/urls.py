"""
URL configuration for prefeitura project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("Imposto_e_Certidoes/", views.Imposto_e_Certidoes),
    path("Autorizacao_e_Alvara/", views.Autorizacao_e_Alvara),
    path("SEDURB_Autorizacao/", views.SEDURB_Autorizacao),
    path("SEDURB_Atualizacao/", views.SEDURB_Atualizacao),
    path("Atualizacao_Quiosque/", views.Atualizacao_Quiosque),
    path("mostrar_dados_sedurb_autorizacao/", views.Mostrar_Dados_SEDURB_Autorizacao),
]
