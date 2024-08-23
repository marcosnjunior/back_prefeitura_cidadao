from django.db import models


#PROCON
class Duvida(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=3)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=15)
    cidade = models.CharField(max_length=20)
    telefone_whatsapp = models.CharField(max_length=20)
    email = models.CharField(max_length=75)
    razao_social = models.CharField(max_length=200)
    telefone_fornecedor = models.CharField(max_length=20)
    nome_fts_fncd = models.CharField(max_length=150)
    endereco_fornecedor = models.CharField(max_length=200)
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

class Reclamacao(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=3)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=15)
    cidade = models.CharField(max_length=20)
    telefone_whatsapp = models.CharField(max_length=20)
    email = models.CharField(max_length=75)
    razao_social = models.CharField(max_length=200)
    telefone_fornecedor = models.CharField(max_length=20)
    nome_fts_fncd = models.CharField(max_length=150)
    endereco_fornecedor = models.CharField(max_length=200)
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

class Denuncia(models.Model):
    descricao = models.CharField(max_length=250)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=3)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=15)
    cidade = models.CharField(max_length=20)
    telefone_whatsapp = models.CharField(max_length=20)
    email = models.CharField(max_length=75)
    razao_social = models.CharField(max_length=200)
    telefoneFornecedor = models.CharField(max_length=20)
    nomeFornencedor = models.CharField(max_length=150)
    enderecoFornecedor = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao

#PÂO E LEITE
class PaoLeite(models.Model):
    nome = models.CharField(max_length=150)
    dataNascimento =  models.CharField(max_length=150)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=20)
    carteiraTrabalhoAss = models.CharField(max_length=1)
    possuiDeficiencia = models.CharField(max_length=1)
    estadoCivil = models.CharField(max_length=1)
    numeroNis = models.CharField(max_length=50)
    possuiBolsaFamilia = models.CharField(max_length=1)
    possuiCartaoAlimentacao = models.CharField(max_length=1)
    concordoTermos = models.CharField(max_length=1)

    def __str__(self):
        return self.nome

#SALA DO EMPREENDEDOR
class EmissaoBoleto(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=75)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    observacoes = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

# Create your models here.