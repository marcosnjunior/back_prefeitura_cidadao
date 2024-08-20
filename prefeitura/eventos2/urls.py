from django.urls import path
from . import views

urlpatterns = [
   # path('', views.procon),
   path('procon', views.procon),
   path('duvida',views.duvida),
   path('reclamacao',views.reclamacao),
   path('denuncia', views.denuncia),
   path('paoleite', views.paoleite),
   path('cras', views.cras),
   path('textocras', views.textocras),
   path('formpaoleite', views.formpaoleite),
   
]