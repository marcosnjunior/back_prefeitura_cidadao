from django.shortcuts import render, redirect
from .models import Recebimento_de_Convite, Solicitacao_de_Apoio, Solicitacao_de_Material,  Solicitacao_de_Reparos_e_Manutencao_de_Equipamentos, Solicitacao_de_Uso_de_Espaco_Fisico

# Create your views here.
def esporte(request):
    return render(request, 'esporte.html')

def recebimento_de_Convites(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Recebimento_de_Convite.objects.create(descricao=descricao)
        return redirect("/esporte")
    else:
        return render(request, 'recebimento_de_convite.html')

def solicitacao_de_Apoio(request):
     if request.method == "POST":
        descricao = request.POST.get('descricao')
        Solicitacao_de_Apoio.objects.create(descricao=descricao)
        return redirect("/esporte")
     else:
        return render(request, 'solicitacao_de_apoio.html')


def solicitacao_de_Material(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Solicitacao_de_Material.objects.create(descricao=descricao)
        return redirect("/esporte")
    else:
        return render(request, 'solicitacao_de_material.html')


def solicitacao_de_Reparos_e_Manutencao_de_Equipamentos(request):
     if request.method == "POST":
        descricao = request.POST.get('descricao')
        Solicitacao_de_Reparos_e_Manutencao_de_Equipamentos.objects.create(descricao=descricao)
        return redirect("/esporte")
     else:
        return render(request, 'solicitacao_de_reparos_e_manutencao_de_equipamentos.html')
     
def solicitacao_de_Uso_de_Espaco_Fisico(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        Solicitacao_de_Uso_de_Espaco_Fisico.objects.create(descricao=descricao)
        return redirect("/esporte")
    else:
        return render(request, 'solicitacao_de_uso_de_espaco_fisico.html')
    
def esporte_admin(request):
    resultado = Recebimento_de_Convite.objects.all()

    return render(request, 'esporte_admin.html', {"resultado": resultado})
    