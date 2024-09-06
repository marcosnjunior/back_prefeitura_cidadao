from django.urls import path
from . import views

urlpatterns = [
   
   path('procon', views.procon, name='procon'),
   path('duvida',views.duvida, name='duvida'),
   path('reclamacao',views.reclamacao, name='reclamacao'),
   path('denuncia', views.denuncia, name='denuncia'),
   path('paoleite', views.paoleite, name='paoleite'),
   path('cras', views.cras, name='cras'),
   path('textocras', views.textocras, name='textocras'),
   path('formpaoleite', views.formpaoleite, name='formpaoleite'),
   path('admin_eventos2', views.admin_eventos2, name='admin_eventos2'),
]