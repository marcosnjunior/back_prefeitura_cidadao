from django.db import models
#from django.utils import timezone

class Cultura (models.Model):
    
    class Meta:
        verbose_name = 'Cultura'



class Funjope_Apoio_a_eventos_artisticos (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Apoio a Eventos Artisticos e Culturais'


class Funjope_atestado_da_condicao_de_artista_local (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Atestado da Condição de Artista Local'


class Funjope_cadastramento_de_artistas_e_outros (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Cadastramento de Artistas e Outros'


class Funjope_concertos_de_orquestra_sinfonica (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Concertos de Orquestra Sinfônica Municipal de João Pessoa (OSMJP)'


class Funjope_exposicao_de_artes_visuais (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Exposição de Artes Visuais, Oficinas Culturais, Seminários e Palestras'


class Funjope_edital_de_ocupacao_do_casa_da_polvora (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Edital de Ocupação do Casa da Pólvora'


class Funjope_edital_de_ocupacao_do_casarao_34 (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Edital de Ocupação do Casarão 34'


class Funjope_edital_de_ocupacao_do_hotel_globo (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Edital de Ocupação do Hotel Globo'


class Funjope_instalacao_de_obras_de_arte (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Instalação de Obras de Arte'


class Funjope_jp_cultura (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - JP Cultura'


class Funjope_jp_film_commission (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - JP Film Commission'


class Funjope_lei_dos_edificios (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Lei dos Edifícios'


class Funjope_prestacao_de_contas (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Prestação de Contas"'


class Funjope_projeto_acao_social_pela_musica (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Projeto Ação Social pela Música'


class Funjope_solicitacao_de_pagamento (models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'FUNJOPE - Solicitação de Pagamento'



###############################################################################



class Conselho_tutelar (models.Model):
    
    class Meta:
        verbose_name = 'Conselho Tutelar'



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


###################################################################


class Familia_acolhedora (models.Model):

    class Meta:
        verbose_name = 'Família Acolhedora'

class Familia_acolhedora_forms (models.Model):
    nome = models.CharField(max_length=100, default='null')
    idade = models.IntegerField(default=0)
    data_nascimento = models.IntegerField(default=0)
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