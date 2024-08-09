from django.shortcuts import render, redirect

from .forms import *
# Create your views here.

def apreensao_base(request):
    return render(request, "apreensaodeanimais.html")

def saudeanimal_base(request):
    return render(request, "saudeanimal.html")

def bemestaranimal_base(request):
    return render(request, "bemestaranimal.html")

def coleta(request):
    if request.method == "POST":
        form = ColetaAnimaisMortosForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/animais/apreensao-de-animal")
    else:
        form = ColetaAnimaisMortosForm()

    return render(request, "ColetaAnimaisMortos.html", {"form": form})

def Apreensao(request):
    if request.method == "POST":
        form = ApreensaoAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/animais/apreensao-de-animal")
    else:
        form = ApreensaoAnimalForm()

    return render(request, "ApreensaoAnimal.html", {"form": form})

def Denuncia(request):
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/animais/saude-animal")
    else:
        form = DenunciaForm()

    return render(request, "Denuncia.html", {"form": form})

def AgendaConsulta(request):
    if request.method == "POST":
        form = AgendaConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/animais/bem-estar-animal")
    else:
        form = AgendaConsultaForm()

    return render(request, "AgendaConsulta.html", {"form": form})

def AgendaCastracao(request):
    if request.method == "POST":
        form = AgendaCastracaoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/animais/bem-estar-animal")
    else:
        form = AgendaCastracaoForm()

    return render(request, "AgendaCastracao.html", {"form": form})

def HospitalVeterinario(request):
    if request.method == "POST":
        form = HospitalVeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/animais/bem-estar-animal")
    else:
        form = HospitalVeterinarioForm()

    return render(request, "HospitalVeterinario.html", {"form": form})

