from django.db import models
#from django.utils import timezone

class Cultura (models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome


class Conselho_tutelar (models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    

class Ptts_ouvidoria (models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    

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