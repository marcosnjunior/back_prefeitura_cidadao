from django.db import models

STATUS = {
    'Aberto': 'Aberto',
    'Em Andamento': 'Em Andamento',
    'Fechado': 'Fechado',
}

# Create your models here.
class Autorizacao_de_Estagio_Supervisionado(models.Model):
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='Aberto')

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEDEC - Autorização de Estágio Supervisionado'

class Autorizacao_para_Pesquisa_CREI_Escola(models.Model):
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='Aberto')

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEDEC - Autorização para Pesquisa CREI/Escola'

class Furto_Extravio_ou_Perda_de_Equipamentos(models.Model):
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='Aberto')

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEDEC - Furto, Extravio, ou Perda de Equipamentos'

class Solicitacao_de_Espaco_Fisico_Escola_CREI(models.Model):
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='Aberto')

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEDEC - Solicitação de Espaço Físico - Escola/CREI'

class Solicitacao_Diversa(models.Model):
    descricao = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='Aberto')

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'SEDEC - Solicitação Diversa'
