from django.shortcuts import render
from django.http import HttpResponse
from .models import SEDRUB_Autorizacao_Uso_Solo_Comercial, Autorizacao_Uso_de_Solo_Eventual, Atualizacao_Cadatral_Dos_Quiosques

def Mostrar_Dados_SEDURB_Autorizacao(request):
    dados = SEDRUB_Autorizacao_Uso_Solo_Comercial.objects.all()
    return render(request, 'Mostrar_Dados_SEDURB_AUTORIZACAO.html', {'dados': dados})
    # Criar um dicionário com a variável e outros dados necessários


def Imposto_e_Certidoes(request): # VIEW PARA CARREGAR A PAGINA
    # return HttpResponse('<h1>Hello HttpResponse</h1>')
    return render(request, 'Imposto_e_Certidoes.html', {})

def Autorizacao_e_Alvara(request):
    return render(request, 'Autorização e Alvara (SEDURBs).html')

def SEDURB_Atualizacao(request):
    if request.method == 'POST':
        Formulario = Autorizacao_Uso_de_Solo_Eventual()
        Formulario.Descricao = request.POST.get('Descricao')
        Formulario.Requerente = request.POST.get('Requerente')
        Formulario.CPF = request.POST.get('CPF')
        Agua = request.POST.get('Lig_Agua')
        Energia = request.POST.get('Lig_Energ')
            
        if Agua == None: Agua = False
        else: Agua = True
        
        if Energia == None: Energia = False
        else: Energia = True

        Formulario.Ligação_de_Água = Agua
        Formulario.Ligação_de_Energia = Energia
        Formulario.Endereco = request.POST.get('Endereco')
        Formulario.save()  

    return render(request, 'SEDURB_Atualizacao (SEDURBs).html')

def Atualizacao_Quiosque(request): # FORMULARIO QUIOSQUES
    if request.method == 'POST':
        Formulario = Atualizacao_Cadatral_Dos_Quiosques()
        Formulario.Caixa1 = request.POST.get('caixa1')
        Formulario.Nome = request.POST.get('Nome')
        Formulario.CPF = request.POST.get('CPF')
        Formulario.Telefone = request.POST.get('Telefone')
        Formulario.Email = request.POST.get('Email')
        Formulario.Endereco_1 = request.POST.get('Endereco_1')
        Formulario.Endereco_2 = request.POST.get('Endereco_2')
        Formulario.Logradouro = request.POST.get('Logradouro')
        Formulario.Bairro = request.POST.get('Bairro')
        Formulario.Tipo_Equipamento = request.POST.get('Tipo_Equipamento')
        Formulario.Numero_Box = request.POST.get('Numero_Box')
        Formulario.Quadra_ou_ilha = request.POST.get('Quadra_ou_ilha')
        Formulario.Tipo_Construcao = request.POST.get('Tipo_Construcao')
        Formulario.Area_Ocupada = request.POST.get('Area_Ocupada')
        Formulario.Tempo_Ocupa = request.POST.get('Tempo_Ocupa')
        Formulario.Validade_Permissao = request.POST.get('Validade_Permissao')
        Formulario.Estrutura_Utilizada = request.POST.get('Estrutura_Utilizada')
        Formulario.Atividade_Economica = request.POST.get('Atividade_Economica')
        Formulario.Infor_1 = request.POST.get('Infor')
        Formulario.Descricao = request.POST.get('Descricao')
        Formulario.save()
    return render(request, 'Autorizacao_Quiosques.html')

def SEDURB_Autorizacao(request):
    if request.method == 'POST': 
        Formulario_SEDRUB = SEDRUB_Autorizacao_Uso_Solo_Comercial()
        Formulario_SEDRUB.Descricao = request.POST.get('Descricao')
        Formulario_SEDRUB.Requerente = request.POST.get('Requerente')
        Formulario_SEDRUB.CPF = request.POST.get('CPF')
        Agua = request.POST.get('Lig_Agua')
        Energia = request.POST.get('Lig_Energ')

        Status = request.POST.get('Status')
        
        if Agua == None: Agua = False
        else: Agua = True
        
        if Energia == None: Energia = False
        else: Energia = True

        Formulario_SEDRUB.Ligação_de_Água = Agua
        Formulario_SEDRUB.Ligação_de_Energia = Energia
        Formulario_SEDRUB.Endereco = request.POST.get('Endereco')
        Formulario_SEDRUB.Status = request.POST.get('Status')
        Formulario_SEDRUB.save()   
    else:
        print('\n Não entrou')

    return render(request, 'SEDURB - Autorização Uso de Solo - Comercial.html', {})

# Create your views here.
