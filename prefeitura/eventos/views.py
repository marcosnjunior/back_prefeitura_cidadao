from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cultura, Funjope_Apoio_a_eventos_artisticos, Conselho_tutelar, Conselho_tutelar_cristo, Conselho_tutelar_mangabeira, Conselho_tutelar_norte, Conselho_tutelar_praia, Conselho_tutelar_sudeste, Conselho_tutelar_sul, Conselho_tutelar_valentina, Ptts_ouvidoria_maria_de_nazare, Familia_acolhedora
from django.db.models import Q 


def eventos(request):
    #return HttpResponse("chegou em eventos") 
    #return render(request, 'eventos/eventos.html', {})
    return render(request, 'home.html', {})


def familia_acolhedora(request):

    #return HttpResponse("chegou nas views -> familia_acolhedora")
    return render(request, 'eventos/familia_acolhedora.html', {})


def familia_acolhedora_(request):

    if request.method == "POST":
        
        data_nascimneto = request.POST.get('data_nascimneto')
        print(data_nascimneto)

        cpf = request.POST.get('cpf')
        print(cpf)


        """
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        data_nascimneto = request.POST.get('data_nascimneto')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        endereco = request.POST.get('endereco')
        numero_residencia = request.POST.get('numero_residencia')
        cep = request.POST.get('cep')
        ponto_referencia = request.POST.get('ponto_referencia')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        complemento = request.POST.get('complemento')
        telefone = request.POST.get('telefone')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        sabendo_servico = request.POST.get('sabendo_servico')
        preferencia_perfil = request.POST.get('preferencia_perfil')
        genero_acolhimento = request.POST.get('genero_acolhimento')
        renda = request.POST.get('renda')
        renda_aproximada = request.POST.get('renda_aproximada')
        residente = request.POST.get('residente')
        mensagem = request.POST.get('mensagem')

        cadastro_familia = Familia_acolhedora()
        cadastro_familia.nome = nome
        cadastro_familia.idade = idade
        cadastro_familia.data_nascimneto = data_nascimneto
        cadastro_familia.cpf = cpf
        cadastro_familia.rg = rg
        cadastro_familia.endereco = endereco
        cadastro_familia.numero_residencia = numero_residencia
        cadastro_familia.cep = cep
        cadastro_familia.ponto_referencia = ponto_referencia
        cadastro_familia.bairro = bairro
        cadastro_familia.cidade = cidade
        cadastro_familia.uf = uf
        cadastro_familia.complemento = complemento
        cadastro_familia.telefone = telefone
        cadastro_familia.celular = celular
        cadastro_familia.email = email
        cadastro_familia.sabendo_servico = sabendo_servico
        cadastro_familia.preferencia_perfil = preferencia_perfil
        cadastro_familia.genero_acolhimento = genero_acolhimento
        cadastro_familia.renda = renda
        cadastro_familia.renda_aproximada = renda_aproximada
        cadastro_familia.residente = residente
        cadastro_familia.mensagem = mensagem
        cadastro_familia.save()
""" 
        return redirect("/eventos/familia_acolhedora")
    
    else:
        return render(request, 'eventos/familia_acolhedora_.html', {})
   

def cultura(request):
    return render(request, 'eventos/cultura.html', {})

def funjope_Apoio_a_eventos_artisticos(request):
    return render(request, 'eventos/funjope_Apoio_a_eventos_artisticos.html')

def cultura_(request):
    return render(request, 'eventos/cultura_.html', {})

######################################################################

def conselho_tutelar(request):
    return render(request, 'eventos/conselho_tutelar.html', {})

def conselho_tutelar_cristo(request):
    return render(request, 'eventos/conselho_tutelar_cristo.html', {})


"""

if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        cadastro = Conselho_tutelar_cristo()
        cadastro = descricao_denuncia
        cadastro = endereco_aconteceu
        cadastro = descricao
        cadastro.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_cristo.html', {})

        
if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        Conselho_tutelar_cristo.objects.create(descricao_denuncia=descricao_denuncia)
        Conselho_tutelar_cristo.objects.create(endereco_aconteceu=endereco_aconteceu)
        Conselho_tutelar_cristo.objects.create(descricao=descricao)

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_cristo.html', {})
"""


def conselho_tutelar_mangabeira(request):
    return render(request, 'eventos/conselho_tutelar_mangabeira.html', {})

def conselho_tutelar_norte(request):
    return render(request, 'eventos/conselho_tutelar_norte.html', {})

def conselho_tutelar_praia(request):
    return render(request, 'eventos/conselho_tutelar_praia.html', {})

def conselho_tutelar_sudeste(request):
    return render(request, 'eventos/conselho_tutelar_sudeste.html', {})

def conselho_tutelar_sul(request):
    return render(request, 'eventos/conselho_tutelar_sul.html', {})

def conselho_tutelar_valentina(request):
    return render(request, 'eventos/conselho_tutelar_valentina.html', {})

def conselho_tutelar_denuncia(request):
    return render(request, 'eventos/conselho_tutelar_denuncia.html', {})


#######################################################################################

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