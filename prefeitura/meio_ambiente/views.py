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
            return redirect('/meio_ambiente/plantio_de_arvores')
    else:
        form = Plantio_de_ArvoreForm()
    return render(request, 'plantio_de_arvores.html', {'form': form})
