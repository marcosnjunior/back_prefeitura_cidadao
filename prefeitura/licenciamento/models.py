from django.db import models

class IPTU_Isencao_Imoveis(models.Model): # ATUALIZACAO
    Descricao = models.TextField()

    def __str__(self):
        return self.Descricao

class ISS_Reduçãode_Alíquota_ISS(models.Model):
    Descricao = models.TextField()

    def __str__(self):
        return self.Descricao

# Create your models here.
