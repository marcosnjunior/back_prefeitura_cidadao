from django.db import models

# Create your models here.

class Recebimento_de_Convite(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEJER - Recebimento_de_Convite'
    
class Solicitacao_de_Apoio(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEJER - Solicitacao_de_Apoio'

class Solicitacao_de_Material(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEJER - Solicitacao_de_Material'

class Solicitacao_de_Reparos_e_Manutencao_de_Equipamentos(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEJER - Solicitacao_de_Reparos_e_Manutencao_de_Equipamentos'

class Solicitacao_de_Uso_de_Espaco_Fisico(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEJER - Solicitacao_de_Uso_de_Espaco_Fisico'


