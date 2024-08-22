from django.shortcuts import render,redirect
from .forms import *

def home(request):
    return render(request,'iluminacao.html')

def manutencao(request):
    return render(request,'manutencaoVias.html')



def problema_iluminacao(request):
    if request.method == 'POST':
        form = Problema_iluminacaoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/infraestrutura')
    else:
        form = Problema_iluminacaoForm()
    return render(request, 'iluminacao/problema_iluminacao.html', {'form': form})

def expansao_iluminacao(request):
    if request.method == 'POST':
        form = Expansao_iluminacaoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('infraestrutura')
    else:
        form = Expansao_iluminacaoForm()
    return render(request, 'iluminacao/expansao_iluminacao.html', {'form': form})


def tapa_buraco(request):
    if request.method == 'POST':
        form = Tapa_buracoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('infraestrutura')
    else:
        form = Tapa_buracoForm()
    return render(request, 'moblidadeUrbana/tapa_buraco.html', {'form': form})


def galeria_boca_lobo(request):
    if request.method == 'POST':
        form = GaleriaBocaLoboForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('infraestrutura')
    else:
        form = GaleriaBocaLoboForm()
    return render(request, 'moblidadeUrbana/galeria_boca_lobo.html', {'form': form})


def terraplanagem(request):
    if request.method == 'POST':
        form = TerraplanagemForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('infraestrutura')
    else:
        form = TerraplanagemForm()
    return render(request, 'moblidadeUrbana/terraplanagem.html', {'form': form})


