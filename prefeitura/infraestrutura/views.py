from django.shortcuts import render,redirect
from .forms import *

def home(request):
    return render(request,'iluminacao.html')


def problema_iluminacao(request):
    if request.method == 'POST':
        form = Problema_iluminacaoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/infraestrutura')
    else:
        form = Problema_iluminacaoForm()
    return render(request, 'problema_iluminacao.html', {'form': form})

def expansao_iluminacao(request):
    if request.method == 'POST':
        form = Expansao_iluminacaoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('infraestrutura')
    else:
        form = Expansao_iluminacaoForm()
    return render(request, 'expansao_iluminacao.html', {'form': form})


