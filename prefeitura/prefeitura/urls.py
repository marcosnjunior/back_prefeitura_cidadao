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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("educacao/", include("educacao.urls")),
    path("animais/", include("animais.urls")),
    path("saude/", include("saude.urls")),
    path("", include("home.urls")),
    path("esporte/", include("esporte.urls")),
    path("eventos2/", include("eventos2.urls")),
    path("licenciamento/", include("licenciamento.urls")),
    path("infraestrutura/", include("infraestrutura.urls")),
    path("educacao/", include("educacao.urls")),
    path("licenciamento_2/", include("licenciamento_2.urls")),
    path("eventos/", include("eventos.urls")),
    path("meio_ambiente/", include("meio_ambiente.urls")),
    path("zeladoria/", include("zeladoria.urls")),
    path("seguranca/", include("seguranca.urls")),
]
