from django.shortcuts import render, redirect
from .models import Autorizacao_de_Estagio_Supervisionado, Autorizacao_para_Pesquisa_CREI_Escola, Furto_Extravio_ou_Perda_de_Equipamentos, Solicitacao_de_Espaco_Fisico_Escola_CREI, Solicitacao_Diversa

# Create your views here.
def educacao(request):
    return render(request, 'educacao.html')

def autorizacao_de_estagio_supervisionado(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Autorizacao_de_Estagio_Supervisionado.objects.create(descricao=descricao)
        return redirect("/educacao")
    else:
        return render(request, 'autorizacao_de_estagio_supervisionado.html')

def autorizacao_para_pesquisa_crei_escola(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Autorizacao_para_Pesquisa_CREI_Escola.objects.create(descricao=descricao)
        return redirect("/educacao")
    else:
        return render(request, 'autorizacao_para_pesquisa_crei_escola.html')

def furto_extravio_ou_perda_de_equipamentos(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Furto_Extravio_ou_Perda_de_Equipamentos.objects.create(descricao=descricao)
        return redirect("/educacao")
    else:
        return render(request, 'furto_extravio_ou_perda_de_equipamentos.html')

def solicitacao_de_espaco_fisico_escola_crei(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Solicitacao_de_Espaco_Fisico_Escola_CREI.objects.create(descricao=descricao)
        return redirect("/educacao")
    else:
        return render(request, 'solicitacao_de_espaco_fisico_escola_crei.html')

def solicitacao_diversa(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Solicitacao_Diversa.objects.create(descricao=descricao)
        return redirect("/educacao")
    else:
        return render(request, 'solicitacao_diversa.html')

def admin(request):
    estagios = Autorizacao_de_Estagio_Supervisionado.objects.all()
    pesquisas = Autorizacao_para_Pesquisa_CREI_Escola.objects.all()
    perdas = Furto_Extravio_ou_Perda_de_Equipamentos.objects.all()
    espacos = Solicitacao_de_Espaco_Fisico_Escola_CREI.objects.all()
    diversas = Solicitacao_Diversa.objects.all()
    return render(request, 'admin.html', {
        'estagios': estagios,
        'pesquisas': pesquisas,
        'perdas': perdas,
        'espacos': espacos,
        'diversas': diversas,
    })
