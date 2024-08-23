from django.shortcuts import render, redirect
from .models import ColetaDePoda, TerrenoSemConservacao, LimpezaDePropriosMunicipais, CataTreco,  DenunciaDeDescarteIrregularDeResiduos, ColetaDeResiduosDiversificados, VarricaoDeLogradourosPublicos, ColetaSeletiva, FalhaNaColetaDomiciliar, ColetaDeAnimaisMortos 

# Create your views here.

def zeladoria(request):
    return render(request, 'zeladoria.html')

def coleta_de_poda(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        coleta_de_poda.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'coleta_de_poda.html')

def terreno_sem_conservacao(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        terreno_sem_conservacao.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'terreno_sem_conservacao.html')

def limpeza_de_proprios_municipais(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        limpeza_de_proprios_municipais.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'limpeza_de_proprios_municipais.html')

def cata_treco(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        cata_treco.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'cata_treco.html')

def denuncia_de_descarte_irregular_de_residuos(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        denuncia_de_descarte_irregular_de_residuos.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'denuncia_de_descarte_irregular_de_residuos.html')

def coleta_de_residuos_diversificados(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        coleta_de_residuos_diversificados.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'coleta_de_residuos_diversificados.html')

def varricao_de_logradouros_publicos(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        varricao_de_logradouros_publicos.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'varricao_de_logradouros_publicos.html')

def coleta_seletiva(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        coleta_seletiva.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'coleta_seletiva.html')

def falha_na_coleta_domiciliar(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        falha_na_coleta_domiciliar.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'falha_na_coleta_domiciliar.html')

def coleta_de_animais_mortos(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        coleta_de_animais_mortos.objects.create(descricao=descricao)
        return redirect("/zeladoria")
    else:
        return render(request, 'coleta_de_animais_mortos.html')











