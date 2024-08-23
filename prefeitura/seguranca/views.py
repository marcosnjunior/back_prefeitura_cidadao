from django.shortcuts import render, redirect
from .models import Palestras_Para_Instituicoes_De_Ensino, Registro_De_Ocorrencia_De_Desastre, Registro_De_Ocorrencia_De_Desastre, Solicitacao_De_Visitorias_Preventivas, Alagamento, Desmoronamento, Secretaria_De_Seguranca_Urbana_Cidadania, Solicitacao_De_Guarnicao_Para_Evento, Solicitacao_De_Rondas_Da_Guarda_Municipal, Teatro_De_Fantoches, Denuncie_aqui

# Create your views here.

def defesa_civil(request):
    return render(request, "defesa_civil.html", {})

def guarda_municipal(request):
    return render(request, "guarda_municipal.html", {})

# Defesa Civil

def palestra(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        palestra = Palestras_Para_Instituicoes_De_Ensino()
        palestra.descricao = descricao

        palestra.save()

        return redirect("/seguranca/defesa-civil")
    
    return render(request, "servicos_defesa_civil/palestra.html", {})

def registro(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        registro = Registro_De_Ocorrencia_De_Desastre()
        registro.descricao = descricao
        registro.save()

        return redirect("/seguranca/defesa-civil")
    
    return render(request, "servicos_defesa_civil/registro_de_ocorrencia_e_desastre.html", {})

def vistoria(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        vistoria = Solicitacao_De_Visitorias_Preventivas()
        vistoria.descricao = descricao
        vistoria.save()

        return redirect("/seguranca/defesa-civil")
    
    return render(request, "servicos_defesa_civil/solicitacao_de_vistorias_preventivas.html", {})

def alagamento(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        alagamento = Alagamento()
        alagamento.descricao = descricao
        alagamento.save()

        return redirect("/seguranca/defesa-civil")
    
    return render(request, "servicos_defesa_civil/alagamento.html", {})

def desmoronamento(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        desmoronamento = Desmoronamento()
        desmoronamento.descricao = descricao
        desmoronamento.save()

        return redirect("/seguranca/defesa-civil")
    
    return render(request, "servicos_defesa_civil/desmoronamento.html", {})



# Guarda Municipal
def secretaria_de_seguranca_urbana_cidadania(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        secretaria = Secretaria_De_Seguranca_Urbana_Cidadania()
        secretaria.descricao = descricao
        secretaria.save()

        return redirect("/seguranca/guarda-municipal")
    
    return render(request, "servicos_guarda_municipal/secretaria_de_seguranca_urbana_cidadania.html", {})

def solicitacao_de_guarnicao(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        solicitacao = Solicitacao_De_Guarnicao_Para_Evento()
        solicitacao.descricao = descricao
        solicitacao.save()

        return redirect("/seguranca/guarda-municipal")
     
    return render(request, "servicos_guarda_municipal/solicitacao_de_guarnicao_para_evento.html", {})

def solicitacao_de_rondas(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        solicitacao = Solicitacao_De_Rondas_Da_Guarda_Municipal()
        solicitacao.descricao = descricao
        solicitacao.save()

        return redirect("/seguranca/guarda-municipal")
    
    return render(request, "servicos_guarda_municipal/solicitacao_de_rondas_da_guarda_municipal.html", {})

def ligue_para_nos(request):
    return render(request, "servicos_guarda_municipal/ligue_para_nos.html", {})

def teatro_de_fantoches(request):
    if request.method == "POST":
        telefone = request.POST.get("telefone_responsavel")
        email = request.POST.get("inserir_email")
        local_apresentacao = request.POST.get("local_apresentacao")
        cep = request.POST.get("inserir_cep")
        bairro = request.POST.get("bairro")
        rua = request.POST.get("inserir_rua")
        referencia = request.POST.get("ponto_referencia")
        publico = request.POST.get("publico_estimado")
        tema_apresentacao = request.POST.get("tema_apresentacao")
        microfone = request.POST.get("microfone")
        som = request.POST.get("caixa_de_som")

        teatro = Teatro_De_Fantoches()
        teatro.telefone_do_resposavel = telefone
        teatro.email = email
        teatro.local_da_apresentacao = local_apresentacao
        teatro.cep = cep
        teatro.bairro = bairro
        teatro.rua = rua
        teatro.ponto_de_referencia = referencia
        teatro.publico_estimado = publico
        teatro.tema_da_apresentacao = tema_apresentacao
        teatro.possui_microfone = microfone
        teatro.possui_caixa_de_som = som
        teatro.save()

        return redirect("/seguranca/guarda-municipal")
    
    return render(request, "servicos_guarda_municipal/teatro_de_fantoches.html", {})

def ouvidoria(request):
    return render(request, "servicos_guarda_municipal/ouvidoria.html", {})

def denuncie_aqui(request):
    if request.method == "POST":
        bairro = request.POST.get("bairro_denuncia")
        rua = request.POST.get("rua_denuncia")
        referencia = request.POST.get("ponto_referencia")
        cep = request.POST.get("cep_denuncia")
        observacoes = request.POST.get("observacoes")
        
        denuncie = Denuncie_aqui()
        denuncie.bairro_do_local_da_denuncia = bairro
        denuncie.rua_do_local_da_denuncia = rua
        denuncie.ponto_de_referencia_do_local_da_denuncia = referencia
        denuncie.cep_do_local_da_denuncia = cep
        denuncie.observacoes = observacoes
        denuncie.save()
        
        return redirect("/seguranca/guarda-municipal")
    return render(request, "servicos_guarda_municipal/denuncie_aqui.html", {})