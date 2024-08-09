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




    
"""
def home(request):
    return render(request, 'loja/home.html', {})


def cadastrar(request):

    if request.method == "POST":

        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        novo_produto = Produto()
        novo_produto.nome = nome
        novo_produto.preco = preco
        novo_produto.quantidade = quantidade
        novo_produto.save()

    return render(request, 'loja/cadastrar.html', {})



def pesquisar(request):


    if request.method == "POST":
        pesquisa = request.POST.get('pesquisa')
        resultado = Produto.objects.filter(nome__contains=pesquisa) 
        return render(request,'loja/pesquisa.html',{'nome': 'Thiago', 'resultado':resultado})
"""