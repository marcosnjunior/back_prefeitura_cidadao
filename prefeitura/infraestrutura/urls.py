from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("problema_iluminacao",views.problema_iluminacao),
]