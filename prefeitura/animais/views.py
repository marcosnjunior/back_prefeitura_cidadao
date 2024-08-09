from django.shortcuts import render, redirect

from .forms import ColetaAnimaisMortosForm, ApreensaoAnimalForm, DenunciaForm
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

