from django.db import models

# Create your models here.

class ColetaDePoda(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Coleta de Poda'

class TerrenoSemConservacao(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Terreno sem consevacão'

class LimpezaDePropriosMunicipais(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Limpeza de Próprios Municipais'

class CataTreco(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Cata-Treco'

class DenunciaDeDescarteIrregularDeResiduos(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Denúncia De Descarte Irregular De Resíduos'

class ColetaDeResiduosDiversificados(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Coleta de Resíduos Diversificados'

class VarricaoDeLogradourosPublicos(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Varrição de Logradouros Públicos'

class ColetaSeletiva(models.Model):
    descrisao = models.TextField()

    def __str__(self):
        return self.descrisao

    class Meta:
        verbose_name = 'Coleta Seletiva (Condomínio/Empresas)'

class FalhaNaColetaDomiciliar(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Falha na Coleta Domiciliar'

class ColetaDeAnimaisMortos(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Coleta de Animais Mortos'


    
    
    
        
    
    
    
    
    

    

    
