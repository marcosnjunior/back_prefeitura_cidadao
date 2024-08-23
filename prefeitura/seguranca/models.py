from django.db import models

# Create your models here.



# Defesa Civil
class Palestras_Para_Instituicoes_De_Ensino(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao

class Registro_De_Ocorrencia_De_Desastre(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao

class Solicitacao_De_Visitorias_Preventivas(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao

class Alagamento(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao

class Desmoronamento(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao
    
# Guarda Municipal

class Secretaria_De_Seguranca_Urbana_Cidadania(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao

class Solicitacao_De_Guarnicao_Para_Evento(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao
    
class Solicitacao_De_Rondas_Da_Guarda_Municipal(models.Model):
    descricao = models.TextField(max_length=2000);  
    def __str__(self):
        return self.descricao

class Teatro_De_Fantoches(models.Model):
    telefone_do_resposavel = models.TextField(max_length=11)
    email = models.TextField(max_length=300)
    local_da_apresentacao = models.TextField(300)
    cep = models.TextField(max_length=9)
    bairro = models.TextField(max_length=200)
    rua = models.TextField(max_length=200, default="")
    ponto_de_referencia = models.TextField(max_length=200)
    publico_estimado = models.IntegerField()
    tema_da_apresentacao = models.TextField(max_length=200)
    possui_microfone = models.TextField(max_length=3)
    possui_caixa_de_som = models.TextField(max_length=3)

    def __str__(self):
        return self.tema_da_apresentacao

class Denuncie_aqui(models.Model):
    bairro_do_local_da_denuncia = models.TextField(max_length=300)
    rua_do_local_da_denuncia = models.TextField(max_length=300)
    ponto_de_referencia_do_local_da_denuncia = models.TextField(max_length=200)
    cep_do_local_da_denuncia = models.TextField(max_length=30)
    observacoes = models.TextField(max_length=1000, default="")
    def __str__(self):
        return self.rua_do_local_da_denuncia
