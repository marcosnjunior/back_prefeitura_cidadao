from django.db import models
from .choice import *
# Create your models here.

class ColetaAnimaisMortos(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=200)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    pontoRef = models.CharField(max_length=200)
    animal_de_grande_porte = models.CharField(max_length=6, choices=ANIMAL)
    observacoes = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=15)

class ApreensaoAnimal(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=200)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    pontoRef = models.CharField(max_length=200)
    animal_de_grande_porte = models.CharField(max_length=6, choices=ANIMAL)
    observacoes = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=15)

class Denuncia(models.Model):
    relatoDenuncia = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    pontoRef = models.CharField(max_length=200)
    
# class CadrastroDeProtetores(models.Model):

class AgendaConsulta(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    animal_de_grande_porte = models.CharField(max_length=6, choices=ANIMAL)
    
class AgendaCastracao(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    animal_de_grande_porte = models.CharField(max_length=6, choices=ANIMAL)

class HospitalVeterinario(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    animal_de_grande_porte = models.CharField(max_length=6, choices=ANIMAL)