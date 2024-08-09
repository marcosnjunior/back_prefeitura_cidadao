from django.db import models

# Create your models here.

class ColetaAnimaisMortos(models.Model):
    ANIMAL_De_GRANDE_PORTE = [
        ("Cavalo", "Cavalo"),
        ("Boi", "Boi"),
        ("Cabra", "Cabra"),
        ("Porco", "Porco")
    ]
    rua = models.CharField(max_length=200, blank=True)
    numero = models.IntegerField(default=0, blank=True)
    bairro = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    cep = models.CharField(max_length=200, blank=True)
    pontoRef = models.CharField(max_length=200)
    animal_de_grande_porte = models.CharField(max_length=6, choices=ANIMAL_De_GRANDE_PORTE)
    observacoes = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=20)

class ApreensaoAnimal(models.Model):
    ANIMAL_De_GRANDE_PORTE = [
        ("Cavalo", "Cavalo"),
        ("Boi", "Boi"),
        ("Cabra", "Cabra"),
        ("Porco", "Porco")
    ]
    rua = models.CharField(max_length=200, blank=True)
    numero = models.IntegerField(default=0, blank=True)
    bairro = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    cep = models.CharField(max_length=200, blank=True)
    pontoRef = models.CharField(max_length=200)
    animal_de_grande_porte = models.CharField(max_length=6, choices=ANIMAL_De_GRANDE_PORTE, blank=True)
    observacoes = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=20)

class Denuncia(models.Model):
    relatoDenuncia = models.CharField(max_length=200)
    cep = models.CharField(max_length=40, blank=True)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    pontoRef = models.CharField(max_length=200)
    
# class CadrastroDeProtetores(models.Model):

