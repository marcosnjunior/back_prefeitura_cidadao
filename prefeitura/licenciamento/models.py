from django.db import models

class SEDRUB(models.Model): # ATUALIZACAO
    Descricao = models.TextField(default='Conteúdo')
    Requerente = models.CharField(max_length=200)
    CPF = models.IntegerField(default=None)
    Ligação_de_Água = models.BooleanField(default=False)
    Ligação_de_Energia = models.BooleanField(default=False)
    Endereco = models.CharField(max_length=500)

    def __str__(self):
        return self.Requerente

class  Autorizacao_Uso_de_Solo_Eventual(models.Model):
    Descricao = models.TextField(default='Conteúdo')
    Requerente = models.CharField(max_length=200, default=None)
    CPF = models.IntegerField(default=None)
    Ligação_de_Água = models.BooleanField(default=False)
    Ligação_de_Energia = models.BooleanField(default=False)
    Endereco = models.CharField(max_length=500)

    def __str__(self):
        return self.Requerente

class Atualizacao_Cadatral_Dos_Quiosques(models.Model):
        Caixa1 = models.CharField(max_length=200,default=None)
        Nome = models.CharField(max_length=200,default=None)

        CPF = models.IntegerField(default=None)
        Telefone = models.IntegerField(default=None)

        Email = models.EmailField(default=None)

        Endereco_1 = models.CharField(max_length=200,default=None)
        Endereco_2 = models.CharField(max_length=200,default=None)
        Logradouro = models.CharField(max_length=200,default=None)
        Bairro = models.CharField(max_length=200,default=None)
        Tipo_Equipamento = models.CharField(max_length=200,default=None)

        Numero_Box = models.IntegerField(default=None)

        Quadra_ou_ilha = models.CharField(max_length=200,default=None)
        Tipo_Construcao = models.CharField(max_length=100,default=None)

        Area_Ocupada = models.IntegerField(default=None)

        Tempo_Ocupa = models.CharField(max_length=100, default=None)
        Validade_Permissao = models.CharField(max_length=100, default=None)

        Estrutura_Utilizada = models.CharField(max_length=200,default=None)
        Atividade_Economica = models.CharField(max_length=200,default=None)
        Infor_1 = models.CharField(max_length=200,default=None)
        Descricao = models.TextField(default=None)

        def __str__(self):
             return self.Nome

# Create your models here.
