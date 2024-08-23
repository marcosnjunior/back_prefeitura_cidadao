from django.shortcuts import render,redirect
from .forms import *

def home(request):
    return render(request,'iluminacao.html')

def manutencao(request):
    return render(request,'manutencaoVias.html')

def manutencao_pracas(request):
    return render(request,'manutencao_pracas.html')


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
            return redirect('/infraestrutura')
    else:
        form = Expansao_iluminacaoForm()
    return render(request, 'iluminacao/expansao_iluminacao.html', {'form': form})


def tapa_buraco(request):
    if request.method == 'POST':
        form = Tapa_buracoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencaoVias')
    else:
        form = Tapa_buracoForm()
    return render(request, 'moblidadeUrbana/tapa_buraco.html', {'form': form})


def galeria_boca_lobo(request):
    if request.method == 'POST':
        form = GaleriaBocaLoboForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencaoVias')
    else:
        form = GaleriaBocaLoboForm()
    return render(request, 'moblidadeUrbana/galeria_boca_lobo.html', {'form': form})


def terraplanagem(request):
    if request.method == 'POST':
        form = TerraplanagemForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencaoVias')
    else:
        form = TerraplanagemForm()
    return render(request, 'moblidadeUrbana/terraplanagem.html', {'form': form})


def pinturas(request):
    if request.method == 'POST':
        form = PinturasForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencao_pracas')
    else:
        form = PinturasForm()
    return render(request, 'manutencao_pracas/pinturas.html', {'form': form})

def hidraulicos(request):
    if request.method == 'POST':
        form = HidraulicosForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencao_pracas')
    else:
        form = HidraulicosForm()
    return render(request, 'manutencao_pracas/hidraulicos.html', {'form': form})

def eletricos(request):
    if request.method == 'POST':
        form = EletricosForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencao_pracas')
    else:
        form = EletricosForm()
    return render(request, 'manutencao_pracas/eletricos.html', {'form': form})

def serralharia(request):
    if request.method == 'POST':
        form = SerralhariaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencao_pracas')
    else:
        form = SerralhariaForm()
    return render(request, 'manutencao_pracas/serralharia.html', {'form': form})

def jardinagem(request):
    if request.method == 'POST':
        form = JardinagemForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencao_pracas')
    else:
        form = JardinagemForm()
    return render(request, 'manutencao_pracas/jardinagem.html', {'form': form})

def marcenaria(request):
    if request.method == 'POST':
        form = MercenariaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/manutencao_pracas')
    else:
        form = MercenariaForm()
    return render(request, 'manutencao_pracas/marcenaria.html', {'form': form})