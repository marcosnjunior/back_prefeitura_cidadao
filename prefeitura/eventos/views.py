from django.shortcuts import render
from django.http import HttpResponse
#from .models import Produto, Fornecedor
from django.db.models import Q 

def eventos(request):
    #return HttpResponse("chegou em eventos")
    return render(request, 'eventos/eventos.html', {})

def familia_acolhedora(request):

    #return HttpResponse("chegou nas views -> familia_acolhedora")
    return render(request, 'eventos/familia_acolhedora.html', {})

#resultado = Fornecedor.objects.all()
    #return HttpResponse(resultado)