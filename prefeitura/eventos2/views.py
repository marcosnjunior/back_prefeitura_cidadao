from django.shortcuts import render, redirect
from .models import Duvida, Reclamacao, Denuncia, PaoLeite, EmissaoBoleto

#PROCON.
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
    form_duvida.nome = nome
    form_duvida.cpf = cpf
    form_duvida.sexo = sexo
    form_duvida.cep = cep
    form_duvida.rua = rua
    form_duvida.bairro = bairro
    form_duvida.cidade = cidade
    form_duvida.telefone_whatsapp = telefone_whatsapp
    form_duvida.email = email
    form_duvida.razao_social = razao_social
    form_duvida.telefone_fornecedor = telefone_fornecedor
    form_duvida.nome_fts_fncd = nome_fts_fncd
    form_duvida.endereco_fornecedor = endereco_fornecedor
    form_duvida.descricao = descricao
    form_duvida.save()

    return redirect('procon')
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
    form_reclamacao.nome = nome
    form_reclamacao.cpf = cpf
    form_reclamacao.sexo = sexo
    form_reclamacao.cep = cep
    form_reclamacao.rua = rua
    form_reclamacao.bairro = bairro
    form_reclamacao.cidade = cidade
    form_reclamacao.telefone_whatsapp = telefone_whatsapp
    form_reclamacao.email = email
    form_reclamacao.razao_social = razao_social
    form_reclamacao.telefone_fornecedor = telefone_fornecedor
    form_reclamacao.nome_fts_fncd = nome_fts_fncd
    form_reclamacao.endereco_fornecedor = endereco_fornecedor
    form_reclamacao.descricao = descricao
    form_reclamacao.save()
    print(telefone_whatsapp)

    return redirect('procon')
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
    nome_fornecedor = request.POST.get('nome_fornecedor')
    endereco_fornecedor = request.POST.get('endereco_fornecedor')
    cnpj = request.POST.get('cnpj')
    status = request.POST.get('status')
    

    form_denuncia = Denuncia()
    form_denuncia.descricao = descricao
    form_denuncia.nome = nome
    form_denuncia.cpf = cpf
    form_denuncia.telefone_whatsapp = telefone_whatsapp
    form_denuncia.sexo = sexo
    form_denuncia.cep = cep
    form_denuncia.rua = rua
    form_denuncia.bairro = bairro
    form_denuncia.cidade = cidade
    form_denuncia.razao_social = razao_social
    form_denuncia.telefone_fornecedor = telefone_fornecedor
    form_denuncia.nome_fornecedor = nome_fornecedor
    form_denuncia.endereco_fornecedor = endereco_fornecedor
    form_denuncia.cnpj = cnpj
    
    form_denuncia.save()
    

    return redirect('procon')
  else:
    return render(request, 'eventos2/denuncia.html')

#PAO E LEITE
def paoleite(request):
  return render(request, 'eventos2/pao-leite.html')

def formpaoleite(request):
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
    form_paoleite.nome = nome
    form_paoleite. dataNascimento =  dataNascimento
    form_paoleite.idade = idade
    form_paoleite.telefone = telefone
    form_paoleite.cpf = cpf
    form_paoleite.endereco = endereco
    form_paoleite.bairro = bairro
    form_paoleite.carteiraTrabalhoAss  = carteiraTrabalhoAss 
    form_paoleite.possuiDeficiencia = possuiDeficiencia
    form_paoleite.estadoCivil = estadoCivil
    form_paoleite.numeroNis = numeroNis
    form_paoleite.possuiBolsaFamilia  = possuiBolsaFamilia 
    form_paoleite.possuiCartaoAlimentacao= possuiCartaoAlimentacao
    form_paoleite.concordoTermos= concordoTermos
    form_paoleite.save()

    return redirect('paoleite')
  else:
    return render(request, 'eventos2/form-pao-leite.html')

def cras(request):
  print("entrou no cras")
  return render(request, 'eventos2/cras.html', {})

def textocras(request):
  return render(request, 'eventos2/texto-cras.html', {})

def admin_eventos2(request):
  return render(request, 'eventos2/admin_eventos2.html', {})
#Create your views here.
