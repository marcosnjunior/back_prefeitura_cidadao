from django.shortcuts import render, redirect
from .models import Duvida, Reclamacao, Denuncia, PaoLeite, EmissaoBoleto

#PROCON
def procon(request):
  print("entrou no procon")
  return render(request, 'eventos2/procon.html', {})

def duvida(request):
  if request.method == "POST":
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    sexo = request.POST.get('sexo')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    telefone_whatsapp = request.POST.get('telefone_whatsapp') 
    email = request.POST.get('email')
    razao_social = request.POST.get('razao_social')
    telefone_fornecedor = request.POST.get('telefone_fornecedor')
    nome_fts_fncd = request.POST.get('nome_fts_fncd')
    endereco_fornecedor = request.POST.get('endereco_fornecedor')
    descricao = request.POST.get('descricao')

    form_duvida = Duvida()
    form_duvida.save()

    return redirect(request, '/procon')
  else:
    return render(request, 'eventos2/duvida.html')

def reclamacao(request):
  if request.method == "POST":
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    sexo = request.POST.get('sexo')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    telefone_whatsapp = request.POST.get('telefone_whatsapp') 
    email = request.POST.get('email')
    razao_social = request.POST.get('razao_social')
    telefone_fornecedor = request.POST.get('telefone_fornecedor')
    nome_fts_fncd = request.POST.get('nome_fts_fncd')
    endereco_fornecedor = request.POST.get('endereco_fornecedor')
    descricao = request.POST.get('descricao')

    form_reclamacao = Reclamacao()
    form_reclamacao.save()

    return redirect(request, '/procon')
  else:
    return render(request, 'eventos2/reclamacao.html')

def denuncia(request):
  if request.method == "POST":
    descricao = request.POST.get('descricao')
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    telefone_whatsapp = request.POST.get('telefone_whatsapp') 
    sexo = request.POST.get('sexo')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    razao_social = request.POST.get('razao_social')
    telefone_fornecedor = request.POST.get('telefone_fornecedor')
    nome_fts_fncd = request.POST.get('nome_fts_fncd')
    endereco_fornecedor = request.POST.get('endereco_fornecedor')
    cnpj = request.POST.get('cnpj')
    

    form_denuncia = Denuncia()
    form_denuncia.save()

    return redirect(request, '/procon')
  else:
    return render(request, 'eventos2/denuncia.html')

#PAO E LEITE
def paoleite(request):
  if request.method == "POST":
    nome = request.POST.get('nome')
    dataNascimento = request.POST.get('dataNascimento')
    idade = request.POST.get('idade')
    telefone = request.POST.get('telefone')
    cpf = request.POST.get('cpf')
    endereco = request.POST.get('endereco')
    bairro = request.POST.get('bairro')
    carteiraTrabalhoAss = request.POST.get('carteiraTrabalhoAss')
    possuiDeficiencia = request.POST.get('possuiDeficiencia')
    estadoCivil = request.POST.get('estadoCivil')
    numeroNis = request.POST.get('numeroNis')
    possuiBolsaFamilia = request.POST.get('possuiBolsaFamilia')
    possuiCartaoAlimentacao = request.POST.get('possuiBolsaFamilia')
    concordoTermos = request.POST.get('concordoTermos')

    form_paoleite = PaoLeite()
    form_paoleite.save()

    return redirect(request, '/procon')
  else:
    return render(request, 'eventos2/pao-leite.html')

def formpaoleite(request):
  return render(request, 'eventos2/form-pao-leite.html')

def cras(request):
  print("entrou no cras")
  return render(request, 'eventos2/cras.html', {})

def textocras(request):
  return render(request, 'eventos2/texto-cras.html', {})
#Create your views here.
