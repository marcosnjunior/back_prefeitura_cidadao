from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cultura, Conselho_tutelar, Ptts_ouvidoria_maria_de_nazare, Familia_acolhedora
from django.db.models import Q 



def eventos(request):
    #return HttpResponse("chegou em eventos") 
    #return render(request, 'eventos/eventos.html', {})
    return render(request, 'home.html', {})


def familia_acolhedora(request):

    #return HttpResponse("chegou nas views -> familia_acolhedora")
    return render(request, 'eventos/familia_acolhedora.html', {})


def familia_acolhedora_(request):

    #return HttpResponse("chegou nas views -> familia_acolhedora")
    return render(request, 'eventos/familia_acolhedora_.html', {})

#resultado = Fornecedor.objects.all()
    #return HttpResponse(resultado)

def cultura(request):
    return render(request, 'eventos/cultura.html', {})

def cultura_(request):
    return render(request, 'eventos/cultura_.html', {})


def conselho_tutelar(request):
    return render(request, 'eventos/conselho_tutelar.html', {})

def conselho_tutelar_(request):
    return render(request, 'eventos/conselho_tutelar_.html', {})

def ptts_ouvidoria_maria_de_nazare(request):
    return render(request, 'eventos/ptts_ouvidoria_maria_de_nazare.html', {})



def maria_de_nazare(request):

    if request.method == "POST":
        feedback = request.POST.get('feedback')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        cadastro = Ptts_ouvidoria_maria_de_nazare()
        cadastro.feedback = feedback
        cadastro.nome = nome
        cadastro.cpf = cpf
        cadastro.telefone = telefone
        cadastro.save()

        return redirect("/eventos/ptts_ouvidoria_maria_de_nazare")
    
    else:
        return render(request, 'eventos/maria_de_nazare.html', {})

"""
def furto_extravio_ou_perda_de_equipamentos(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Furto_Extravio_ou_Perda_de_Equipamentos.objects.create(descricao=descricao)
        return redirect("/educacao")
    else:
        return render(request, 'furto_extravio_ou_perda_de_equipamentos.html')

"""

    
"""

cadastro.feedback = feedback
        cadastro.nome = nome
        cadastro.cpf = cpf
        cadastro.telefone = telefone
        cadastro.save()


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