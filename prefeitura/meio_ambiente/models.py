from django.db import models

#   Plantio de Árvores 

class Plantio_de_Arvores(models.Model):
    larg_compr_calcada = models.CharField(max_length=100)
    observacoes = models.TextField()
    cep = models.IntegerField()
    bairro = models.CharField(max_length=100)
    nome_rua = models.CharField(max_length=100)
    ponto_refer = models.CharField(max_length=100)

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
