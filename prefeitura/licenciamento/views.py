from django.shortcuts import render
from django.http import HttpResponse
from .models import IPTU_Isencao_Imoveis, ISS_Reduçãode_Alíquota_ISS

def IPTU_Isencao_de_Imoveis(request):
    if request.method == 'POST':
        PegarDados = IPTU_Isencao_Imoveis()
        PegarDados.Descricao = request.POST.get('descricao')
        PegarDados.save()
    return render(request, 'Formulario - IPTU_Isencao_Imoveis.html')

def ISS_Redução_de_Alíquota_ISS(request):
    if request.method == 'POST':
        pegarDados = ISS_Reduçãode_Alíquota_ISS()
        pegarDados.Descricao = request.POST.get('descricao')
        pegarDados.save()
    return render(request, 'ISS_Reduçãode_Alíquota_ISS.html')

def previdencia(request):
    return render(request, 'previdencia.html')

def Viva_O_Centro(request):
    return render(request, 'Viva_O_Centro.html')

def iptu(request):
    return render(request, 'iptu.html')
# Create your views here.
