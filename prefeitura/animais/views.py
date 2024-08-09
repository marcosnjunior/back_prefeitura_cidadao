from django.shortcuts import render, redirect

from .forms import *
# Create your views here.

def coleta(request):
    if request.method == "POST":
        form = ColetaAnimaisMortosForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/thanks/")
    else:
        form = ColetaAnimaisMortosForm()

    return render(request, "ColetaAnimaisMortos.html", {"form": form})

def Apreensao(request):
    if request.method == "POST":
        form = ApreensaoAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/thanks/")
    else:
        form = ApreensaoAnimalForm()

    return render(request, "ApreensaoAnimal.html", {"form": form})

def Denuncia(request):
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/thanks/")
    else:
        form = DenunciaForm()

    return render(request, "Denuncia.html", {"form": form})

def AgendaConsulta(request):
    if request.method == "POST":
        form = AgendaConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/thanks/")
    else:
        form = AgendaConsultaForm()

    return render(request, "AgendaConsulta.html", {"form": form})

def AgendaCastracao(request):
    if request.method == "POST":
        form = AgendaCastracaoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/thanks/")
    else:
        form = AgendaCastracaoForm()

    return render(request, "AgendaCastracao.html", {"form": form})

def HospitalVeterinario(request):
    if request.method == "POST":
        form = HospitalVeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect("/thanks/")
    else:
        form = HospitalVeterinarioForm()

    return render(request, "HospitalVeterinario.html", {"form": form})

