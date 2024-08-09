from django.db import models
#from django.utils import timezone

class Familia_acolhedora (models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome

#modelo do banco
"""
class Fornecedor (models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)
    idade = models.DateField()

    def __str__(self):
        return self.nome
"""