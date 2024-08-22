from django.db import models
#from django.utils import timezone

class Cultura (models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Cultura'

##########################################################

class Conselho_tutelar (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Conselho Tutelar'


class Funjope_Apoio_a_eventos_artisticos (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Apoio a Eventos Artisticos e Culturais'


class Conselho_tutelar_cristo (models.Model):
    descricao_denuncia = models.CharField(max_length=300)
    endereco_aconteceu = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Conselho Tutelar Cristo'



class Conselho_tutelar_mangabeira (models.Model):
    descricao_denuncia = models.CharField(max_length=300)
    endereco_aconteceu = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Conselho Tutelar Mangabeira'


class Conselho_tutelar_norte (models.Model):
    descricao_denuncia = models.CharField(max_length=300)
    endereco_aconteceu = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Conselho Tutelar Norte'



class Conselho_tutelar_praia (models.Model):
    descricao_denuncia = models.CharField(max_length=300)
    endereco_aconteceu = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Conselho Tutelar Praia'



class Conselho_tutelar_sudeste (models.Model):
    descricao_denuncia = models.CharField(max_length=300)
    endereco_aconteceu = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Conselho Tutelar Sudeste'



class Conselho_tutelar_sul (models.Model):
    descricao_denuncia = models.CharField(max_length=300)
    endereco_aconteceu = models.CharField(max_length=300)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Conselho Tutelar Sul'



class Conselho_tutelar_valentina (models.Model):
    descricao = models.CharField(max_length=500)
    endereco_aconteceu = models.CharField(max_length=300)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Conselho Tutelar Valentina'


##########################################################



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
    nome = models.CharField(max_length=100, default='null')
    idade = models.IntegerField(default=0)
    data_nascimneto = models.IntegerField(default=0)
    cpf = models.IntegerField(default=0)
    rg = models.IntegerField(default=0)
    endereco = models.CharField(max_length=300, default='null')
    numero_residencia = models.IntegerField(default=0)
    cep = models.IntegerField(default=0)
    ponto_referencia = models.CharField(max_length=200, default='null')
    bairro = models.CharField(max_length=150, default='null')
    cidade = models.CharField(max_length=150, default='null')
    uf = models.CharField(max_length=10, default='null')
    complemento = models.CharField(max_length=200, default='null')
    telefone = models.IntegerField(default=0)
    celular = models.IntegerField(default=0)
    email = models.CharField(max_length=150, default='null')
    sabendo_servico = models.CharField(max_length=150, default='null')
    preferencia_perfil = models.TextField(default='null')
    genero_acolhimento = models.CharField(max_length=20, default='null')
    renda = models.CharField(max_length=5, default='null')
    renda_aproximada = models.CharField(max_length=100, default='null')
    residente = models.CharField(max_length=5, default='null')
    mensagem = models.TextField(default='null')


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