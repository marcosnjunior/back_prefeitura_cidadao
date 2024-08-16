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
            return redirect('/meio_ambiente/poda_de_arvores')
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
            return redirect('/meio_ambiente/lancamento_de_aguas')
    else:
        form = lancamento_de_agua_servidasForm()
    return render(request, 'lancamento_agua_servidas.html', {'form': form})

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
