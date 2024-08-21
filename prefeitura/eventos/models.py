from django.db import models
#from django.utils import timezone

class Cultura (models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Cultura'


class Conselho_tutelar (models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Conselho Tutelar'

class Ptts_ouvidoria_maria_de_nazare (models.Model):
    feedback = models.TextField()
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'PTTS - Ouvidoria - Maria de Nazaré'



class Familia_acolhedora (models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_nascimneto = models.IntegerField()
    cpf = models.IntegerField()
    rg = models.IntegerField()
    endereco = models.CharField(max_length=300)
    numero_residencia = models.IntegerField()
    cep = models.IntegerField()
    ponto_referencia = models.CharField(max_length=200)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    uf = models.CharField(max_length=10)
    complemento = models.CharField(max_length=200)
    telefone = models.IntegerField()
    celular = models.IntegerField()
    email = models.CharField(max_length=150)
    sabendo_servico = models.CharField(max_length=150)
    preferencia_perfil = models.TextField()
    genero_acolhimento = models.CharField(max_length=20)
    renda = models.CharField(max_length=5)
    renda_aproximada = models.CharField(max_length=100)
    residente = models.CharField(max_length=5)
    bem_maior = models.TextField()


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Família Acolhedora'
    


#modelo do banco
"""
class Fornecedor (models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)
    idade = models.DateField()

    def __str__(self):
        return self.nome
"""