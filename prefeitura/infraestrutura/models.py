from django.db import models
from .enums_choices import *



class Problema_iluminacao(models.Model):
    tipo_iluminacao= models.CharField(max_length=15,choices=TIPO_LAMPADA)
    qual_problema_iluminacao =models.CharField(max_length=30,choices=PROBLEMA_ILUMINACAO_CHOICES)
   
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numeroRecidencia = models.IntegerField()
    cep = models.CharField(max_length=10)
    pontoReferencia = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    
class Expansao_iluminacao(models.Model):
    pontoReferencia = models.CharField(max_length=100)
    expansao_iluminacao =models.CharField(max_length=30,choices=EXPANSAO_ILUNUMINACAO)
    rua = models.CharField(max_length=100)
    numeroRecidencia = models.IntegerField()
    bairro = models.CharField(max_length=100)
    estadoUF = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    telefone = models.CharField(max_length=15)


class Tapa_buraco(models.Model):
    pontoReferencia = models.CharField(max_length=100)
    tipo_pavimentacao =models.CharField(max_length=30,choices=TIPO_PAVIMENTACAO)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    numeroRecidencia = models.IntegerField()
    bairro = models.CharField(max_length=100)
    estadoUF = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

class GaleriaBocaLobo(models.Model):
    pontoReferencia = models.CharField(max_length=100)
    problema_Drenagem =models.CharField(max_length=40,choices=PROBLEMA_DRENAGEM)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    numeroRecidencia = models.IntegerField()
    bairro = models.CharField(max_length=100)
    estadoUF = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)


class Terraplanagem(models.Model):
    pontoReferencia = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    numeroRecidencia = models.IntegerField()
    bairro = models.CharField(max_length=100)
    estadoUF = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

    
class Pinturas(models.Model):
    telefone = models.CharField(max_length=15)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    pontoReferencia = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    nome_Area_publica = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_Area_publica
    
class Hidraulicos(models.Model):
    telefone = models.CharField(max_length=15)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    pontoReferencia = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    nome_Area_publica = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_Area_publica
    
class Eletricos(models.Model):
    telefone = models.CharField(max_length=15)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    pontoReferencia = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    nome_Area_publica = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_Area_publica
    
class Serralharia(models.Model):
    telefone = models.CharField(max_length=15)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    pontoReferencia = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    nome_Area_publica = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_Area_publica

class Jardinagem(models.Model):
    telefone = models.CharField(max_length=15)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    pontoReferencia = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    nome_Area_publica = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_Area_publica
    
class Mercenaria(models.Model):
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    observacoes = models.CharField(max_length=255,null=True,default='',blank=True)
    pontoReferencia = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    def __str__(self):
        return self.cep
    

class SEMOB_Apoio_Evento(models.Model):
    observacoes = models.CharField(max_length=255)
    def __str__(self):
        return self.observacoes
    
class SEMOB_Baixa_multa_transito_pagamento(models.Model):
    observacoes = models.CharField(max_length=255)
    def __str__(self):
        return self.observacoes
    
class SEMOB_Baixa_multa_transporte_pagamento(models.Model):
    observacoes = models.CharField(max_length=255)
    def __str__(self):
        return self.observacoes

class SEMOB_Baixa_multa_deferimento_recurso(models.Model):
    observacoes = models.CharField(max_length=255)
    def __str__(self):
        return self.observacoes
    

class SEMOB_Baixa_Certidoes_IPI_ICMS(models.Model):
    observacoes = models.CharField(max_length=255)
    def __str__(self):
        return self.observacoes
    

class SEMOB_Cadastro_Acompanhante_Escolar(models.Model):
    observacoes = models.CharField(max_length=255)
    def __str__(self):
        return self.observacoes