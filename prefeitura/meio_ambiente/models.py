from django.db import models

#   Plantio de Árvores 

class Plantio_de_Arvores(models.Model):
    larg_compr_calcada = models.CharField(max_length=100)
    observacoes = models.TextField()
    cep = models.IntegerField()
    bairro = models.CharField(max_length=100)
    nome_rua = models.CharField(max_length=100)
    ponto_refer = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.bairro



#   Poda de Árvores

class Poda_de_Arvores(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    cep = models.IntegerField()
    ponto_refer = models.CharField(max_length=100)
    observacoes = models.TextField(max_length=100)
    telefone = models.IntegerField()

    def __str__(self):
        return self.rua

class lancamento_de_agua_servidas(models.Model):
    cep_problema = models.IntegerField()
    bairro_problema = models.CharField(max_length=200)
    rua_problema = models.CharField(max_length=200)
    ponto_refer = models.TextField()
    observacoes = models.TextField()

    def __str__(self):
        return self.rua_problema
    
class lancamento_esgoto(models.Model):
    cep_problema = models.IntegerField()
    bairro_problema = models.CharField(max_length=200)
    rua_problema = models.CharField(max_length=200)
    ponto_refer = models.TextField()
    observacoes = models.TextField()

    def __str__(self):
        return self.rua_problema
    
class poluicao_sonora(models.Model):
    observacoes = models.TextField()
    cep_problema = models.IntegerField()
    bairro_problema = models.CharField(max_length=200)
    rua_problema = models.CharField(max_length=200)
    ponto_refer = models.TextField()

    def __str__(self):
        return self.rua_problema

class corte_irregular_arvores(models.Model):
    observacoes = models.TextField()
    cep_problema = models.IntegerField()
    bairro_problema = models.CharField(max_length=200)
    rua_problema = models.CharField(max_length=200)
    ponto_refer = models.TextField()

    def __str__(self):
        return self.rua_problema
    
class poluicao_atmosferica(models.Model):
    observacoes = models.TextField()
    cep_problema = models.IntegerField()
    bairro_problema = models.CharField(max_length=200)
    rua_problema = models.CharField(max_length=200)
    ponto_refer = models.TextField()

    def __str__(self):
        return self.rua_problema
    
class invasao_area_preservacao_permanente(models.Model):
    observacoes = models.TextField()
    cep_problema = models.IntegerField()
    bairro_problema = models.CharField(max_length=200)
    rua_problema = models.CharField(max_length=200)
    ponto_refer = models.TextField()

    def __str__(self):
        return self.rua_problema


