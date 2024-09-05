from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'meio_ambiente.html')
   

def plantio(request):
    if request.method == 'POST':
        form = Plantio_de_ArvoreForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/autorizacao_arborea')
    else:
        form = Plantio_de_ArvoreForm()
    return render(request, 'plantio_de_arvores.html', {'form': form})


def poda(request):
    if request.method == 'POST':
        form = Poda_de_ArvoresForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/autorizacao_arborea')
    else:
        form = Poda_de_ArvoresForm()
    return render(request, 'poda_de_arvores.html', {'form': form})

def denuncia_ambiental(request):
    return render(request, 'denuncia_ambiental.html')



def lancamento(request):
    if request.method == 'POST':
        form = lancamento_de_agua_servidasForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/denuncia_ambiental')
    else:
        form = lancamento_de_agua_servidasForm()
        print("Chegou aqui")
    return render(request, 'lancamento_agua_servidas.html', {'form': form})
    print("não pegou if/else")

def esgoto(request):
    if request.method == 'POST':
        form = lancamento_esgotoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/lancamento_esgoto')
    else:
        form = lancamento_esgotoForm()
    return render(request, 'lancamento_esgoto.html', {'form': form})

def poluicaoSonora(request):
    if request.method == 'POST':
        form = poluicao_sonoraForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/poluicao_sonora')
    else:
        form = poluicao_sonoraForm()
    return render(request, 'poluicao_sonora.html', {'form': form})

def corteIrregularArvores(request):
    if request.method == 'POST':
        form = corte_irregular_arvoresForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/corte_irregular_arvores')
    else:
        form = corte_irregular_arvoresForm()
    return render(request, 'corte_irregular_arvores.html', {'form': form})

def poluicaoAtmosferica(request):
    if request.method == 'POST':
        form = poluicao_atmosfericaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/poluicao_atmosferica')
    else:
        form = poluicao_atmosfericaForm()
    return render(request, 'poluicao_atmosferica.html', {'form': form})

def invasaoAreaPreservacaoPermanente(request):
    if request.method == 'POST':
        form = invasao_area_preservacao_permanenteForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/meio_ambiente/invasao_area_preservacao_permanente')
    else:
        form = invasao_area_preservacao_permanenteForm()
    return render(request, 'invasao_area_preservacao_permanente.html', {'form': form})


def admin_plantio_arvores(request):

    plantio = Plantio_de_Arvores.objects.all()
    return render(request, 'admin_plantio.html', {'plantio' : plantio})
























# produto = Produto.objects.all()
#     return render(request,'loja/pesquisar.html',{'produto': produto})