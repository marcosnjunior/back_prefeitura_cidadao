from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("plantio_de_arvores",views.plantio)
    
]