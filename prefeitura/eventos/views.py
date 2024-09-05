from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cultura, Funjope_Apoio_a_eventos_artisticos, Funjope_atestado_da_condicao_de_artista_local, Funjope_cadastramento_de_artistas_e_outros, Funjope_concertos_de_orquestra_sinfonica, Funjope_exposicao_de_artes_visuais, Funjope_edital_de_ocupacao_do_casa_da_polvora, Funjope_edital_de_ocupacao_do_casarao_34, Funjope_edital_de_ocupacao_do_hotel_globo, Funjope_instalacao_de_obras_de_arte, Funjope_jp_cultura, Funjope_jp_film_commission, Funjope_lei_dos_edificios, Funjope_prestacao_de_contas, Funjope_projeto_acao_social_pela_musica, Funjope_solicitacao_de_pagamento, Conselho_tutelar, Conselho_tutelar_cristo, Conselho_tutelar_mangabeira, Conselho_tutelar_norte, Conselho_tutelar_praia, Conselho_tutelar_sudeste, Conselho_tutelar_sul, Conselho_tutelar_valentina, Ptts_ouvidoria_maria_de_nazare, Familia_acolhedora, Familia_acolhedora_forms
from django.db.models import Q 


def eventos(request):
    #return HttpResponse("chegou em eventos") 
    #return render(request, 'eventos/eventos.html', {})
    return render(request, 'home.html', {})


def familia_acolhedora(request):

    #return HttpResponse("chegou nas views -> familia_acolhedora")
    return render(request, 'eventos/familia_acolhedora.html', {})


def familia_acolhedora_forms(request):

    if request.method == "POST":
      
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        data_nascimento = request.POST.get('data_nascimento')
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

        salvar = Familia_acolhedora_forms()
        salvar.nome = nome
        salvar.idade = idade
        salvar.data_nascimento = data_nascimento
        salvar.cpf = cpf
        salvar.rg = rg
        salvar.endereco = endereco
        salvar.numero_residencia = numero_residencia
        salvar.cep = cep
        salvar.ponto_referencia = ponto_referencia
        salvar.bairro = bairro
        salvar.cidade = cidade
        salvar.uf = uf
        salvar.complemento = complemento
        salvar.telefone = telefone
        salvar.celular = celular
        salvar.email = email
        salvar.sabendo_servico = sabendo_servico
        salvar.preferencia_perfil = preferencia_perfil
        salvar.genero_acolhimento = genero_acolhimento
        salvar.renda = renda
        salvar.renda_aproximada = renda_aproximada
        salvar.residente = residente
        salvar.mensagem = mensagem
        salvar.save()
 
        return redirect("/eventos/familia_acolhedora")
    
    else:
        return render(request, 'eventos/familia_acolhedora_.html', {})
   

##############################################################################


def cultura(request):
    return render(request, 'eventos/cultura.html', {})


def funjope_Apoio_a_eventos_artisticos(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_Apoio_a_eventos_artisticos()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_Apoio_a_eventos_artisticos.html')

    
def funjope_atestado_da_condicao_de_artista_local(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_atestado_da_condicao_de_artista_local()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_atestado_da_condicao_de_artista_local.html')
    

def funjope_cadastramento_de_artistas_e_outros(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_cadastramento_de_artistas_e_outros()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_cadastramento_de_artistas_e_outros.html')


def funjope_concertos_de_orquestra_sinfonica(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_concertos_de_orquestra_sinfonica()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_concertos_de_orquestra_sinfonica.html')


def funjope_exposicao_de_artes_visuais(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_exposicao_de_artes_visuais()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_exposicao_de_artes_visuais.html')
    

def funjope_edital_de_ocupacao_do_casa_da_polvora(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_edital_de_ocupacao_do_casa_da_polvora()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_edital_de_ocupacao_do_casa_da_polvora.html')
    

def funjope_edital_de_ocupacao_do_casarao_34(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_edital_de_ocupacao_do_casarao_34()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_edital_de_ocupacao_do_casarao_34.html')
    

def funjope_edital_de_ocupacao_do_hotel_globo(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_edital_de_ocupacao_do_hotel_globo()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_edital_de_ocupacao_do_hotel_globo.html')
    

def funjope_instalacao_de_obras_de_arte(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_instalacao_de_obras_de_arte()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_instalacao_de_obras_de_arte.html')
    

def funjope_jp_cultura(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_jp_cultura()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_jp_cultura.html')


def funjope_jp_film_commission(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_jp_film_commission()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_jp_film_commission.html')
    

def funjope_lei_dos_edificios(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_lei_dos_edificios()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_lei_dos_edificios.html')
    

def funjope_prestacao_de_contas(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_prestacao_de_contas()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_prestacao_de_contas.html')
    

def funjope_projeto_acao_social_pela_musica(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_projeto_acao_social_pela_musica()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_projeto_acao_social_pela_musica.html')
    

def funjope_solicitacao_de_pagamento(request):

    if request.method == "POST":
        descricao = request.POST.get('descricao')
        salvar = Funjope_solicitacao_de_pagamento()
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/cultura")
    
    else:
        return render(request, 'eventos/funjope_solicitacao_de_pagamento.html')
    

def premio_joao_balula(request):
    return render(request, 'eventos/premio_joao_balula.html')

def edital_de_formento(request):
    return render(request, 'eventos/edital_de_formento.html')



######################################################################

def conselho_tutelar(request):
    return render(request, 'eventos/conselho_tutelar.html', {})


def conselho_tutelar_cristo(request):
        
    if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        salvar = Conselho_tutelar_cristo()
        salvar.descricao_denuncia = descricao_denuncia
        salvar.endereco_aconteceu = endereco_aconteceu
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_cristo.html', {})


def conselho_tutelar_mangabeira(request):

    if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        salvar = Conselho_tutelar_mangabeira()
        salvar.descricao_denuncia = descricao_denuncia
        salvar.endereco_aconteceu = endereco_aconteceu
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_mangabeira.html', {})


def conselho_tutelar_norte(request):

    if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        salvar = Conselho_tutelar_norte()
        salvar.descricao_denuncia = descricao_denuncia
        salvar.endereco_aconteceu = endereco_aconteceu
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_norte.html', {})
    

def conselho_tutelar_praia(request):

    if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        salvar = Conselho_tutelar_praia()
        salvar.descricao_denuncia = descricao_denuncia
        salvar.endereco_aconteceu = endereco_aconteceu
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_praia.html', {})
    

def conselho_tutelar_sudeste(request):

    if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        salvar = Conselho_tutelar_sudeste()
        salvar.descricao_denuncia = descricao_denuncia
        salvar.endereco_aconteceu = endereco_aconteceu
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_sudeste.html', {})
    

def conselho_tutelar_sul(request):

    if request.method == "POST":
        descricao_denuncia = request.POST.get('descricao_denuncia')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        descricao = request.POST.get('descricao')
        salvar = Conselho_tutelar_sul()
        salvar.descricao_denuncia = descricao_denuncia
        salvar.endereco_aconteceu = endereco_aconteceu
        salvar.descricao = descricao
        salvar.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
        return render(request, 'eventos/conselho_tutelar_sul.html', {})
    

def conselho_tutelar_valentina(request):
    
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        endereco_aconteceu = request.POST.get('endereco_aconteceu')
        salvar = Conselho_tutelar_valentina()
        salvar.descricao = descricao
        salvar.endereco_aconteceu = endereco_aconteceu
        salvar.save()

        return redirect("/eventos/conselho_tutelar")
    
    else:
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

