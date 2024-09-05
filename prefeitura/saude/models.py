from django.db import models
# CHOICES
from .choices import *

# vigilancia-sanitaria
class Denuncia(models.Model):
    tipo = models.CharField(max_length=100)
    horarioFuncionamento = models.TimeField()
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    pontoReferencia = models.CharField(max_length=100)
    horaDaDenuncia = models.TimeField()
    motivoDenuncia = models.TextField()
    cidadeDaDenuncia = models.CharField(max_length=100)
    status = models.CharField(max_length=19, choices=TIPO_STATUS_CHOICES, default='Em andamento')

    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name = 'Vigilancia Sanitaria - Denúncia'

# Vacina
class Vacinacao_Domiciliar(models.Model):
   telefone = models.CharField(max_length=15)
   cep = models.CharField(max_length=10)
   bairro = models.CharField(max_length=100)
   rua = models.CharField(max_length=100)
   numeroCasa = models.IntegerField()
   pontoReferencia = models.CharField(max_length=100)
   dataNascimento = models.DateField()
   
   def __str__(self):
       return self.telefone
   
   class Meta:
        verbose_name = 'Vacinação Domiciliar'

# remedio-em-casa

class RemedioEmCasa(models.Model):
    nome = models.CharField(max_length=100)
    numeroCNS = models.IntegerField()
    unidadeSaude = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    estadoUF = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    pacienteAcamado = models.CharField(max_length=1, choices=SIM_OU_NAO)
    dataNascimento = models.DateField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Remédio em Casa'

class RenovacaoReceita(models.Model):
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    pontoReferencia = models.CharField(max_length=100)
    def __str__(self):
        return self.cpf
    class Meta:
        verbose_name = 'Remédio em casa - Renovação de Receita'

# opera-mais

class SoliciteSuaCirugia(models.Model):
    nome = models.CharField(max_length=100)
    sus = models.CharField(max_length=100)
    tipoExame = models.CharField(max_length=2, choices=EXAME_CHOICES)
    informacoesAdicionais = models.TextField()

    def __str__(self):
        return self.nome
   
    class Meta:
        verbose_name = 'Prefeitura opera mais - Solicite sua Cirurgia'

class Exames(models.Model):
    nome = models.CharField(max_length=100)
    sus = models.CharField(max_length=100)
    tipoExame = models.CharField(max_length=2, choices=EXAME_CHOICES)
    informacoesAdicionais = models.TextField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Prefeitura opera mais - Exames'

# LGBT

class Consulta_Ginecologista_LGBT(models.Model):
    nomeSocial = models.CharField(max_length=100)
    nomeRegistro = models.CharField(max_length=100)
    nomeEmergencia = models.CharField(max_length=100)
    cidadeOneReside = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    identidadeGenero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    orientacaoSexual = models.CharField(max_length=2, choices=GENERO_CHOICES)
    cor = models.CharField(max_length=2, choices=COR_CHOICES)
    estadoCivil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES)
    possuiDeficiencia = models.CharField(max_length=1, choices=SIM_OU_NAO)
    tipoDeficiencia = models.CharField(max_length=1, choices=TIPO_DEFICIENCIA_CHOICES, blank=True, null=True)
    tipoViolencia = models.CharField(max_length=1, choices=TIPO_VIOLENCIA_CHOICES, blank=True, null=True)
    motivoViolencia = models.CharField(max_length=2, choices=MOTIVO_VIOLENCIA_CHOICES)
    grauParentesco = models.CharField(max_length=1, choices=GRAU_DE_PARENTESCO_CHOICES)
    localViolencia = models.CharField(max_length=1, choices=LOCAL_DE_VIOLENCIA_CHOICES)
    tenativadeSuicidio = models.CharField(max_length=1, choices=SIM_OU_NAO)
    cpf = models.CharField(max_length=14)
    dataNascimento = models.DateField()
   
    def __str__(self):
           return self.nomeSocial
    
    class Meta:
        verbose_name = 'LGBT - Consulta Ginecologista LGBT'

class Gastroenterologista(models.Model):
    nome = models.CharField(max_length=100)
    nomeRegistro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    identidadeGenero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    orientacaoSexual = models.CharField(max_length=2, choices=GENERO_CHOICES)
    cor = models.CharField(max_length=2, choices=COR_CHOICES)
    estadoCivil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES)
    possuiDeficiencia = models.CharField(max_length=1, choices=SIM_OU_NAO)
    tipoDeficiencia = models.CharField(max_length=1, choices=TIPO_DEFICIENCIA_CHOICES, blank=True, null=True)
    nivelEscolaridade = models.CharField(max_length=2, choices=GRAU_DE_ESCOLARIDADE_CHOICES, null=True)
    trabalhoSituacao = models.CharField(max_length=2, choices=SITUACAO_TRABALHANDO_CHOICES, null=True)
    dataNascimento = models.DateField()
    cpf = models.CharField(max_length=14)
  
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'LGBT - Gastroenterologista'

class ExameCitopatologico(models.Model):
    nome = models.CharField(max_length=100)
    nomeRegistro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    identidadeGenero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    orientacaoSexual = models.CharField(max_length=2, choices=GENERO_CHOICES)
    cor = models.CharField(max_length=2, choices=COR_CHOICES)
    estadoCivil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES)
    localViolencia = models.CharField(max_length=1, choices=LOCAL_DE_VIOLENCIA_CHOICES)
    cpf = models.CharField(max_length=14)
    tipoDeficiencia = models.CharField(max_length=2, choices=TIPO_DEFICIENCIA_CHOICES)
    recebeBeneficio = models.CharField(max_length=2, choices=RECEBE_TIPO_BENEFICIO_CHOICES)
    pensamentoSuicida = models.CharField(max_length=1, choices=SIM_OU_NAO)
    tentativaSuicidio = models.CharField(max_length=1, choices=SIM_OU_NAO)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'LGBT - Exame Citopatológico'

class ExameEndocrinologia(models.Model):
    nome = models.CharField(max_length=100)
    nomeRegistro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    identidadeGenero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    orientacaoSexual = models.CharField(max_length=2, choices=GENERO_CHOICES)
    cor = models.CharField(max_length=2, choices=COR_CHOICES)
    estadoCivil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES)
    localViolencia = models.CharField(max_length=1, choices=LOCAL_DE_VIOLENCIA_CHOICES)
    cpf = models.CharField(max_length=14)
    temDeficiencia = models.CharField(max_length=1, choices=SIM_OU_NAO)
    tipoDeficiencia = models.CharField(max_length=2, choices=TIPO_DEFICIENCIA_CHOICES, blank=True, null=True)
    recebeBeneficio = models.CharField(max_length=2, choices=RECEBE_TIPO_BENEFICIO_CHOICES)
    pensamentoSuicida = models.CharField(max_length=1, choices=SIM_OU_NAO)
    tentativaSuicidio = models.CharField(max_length=1, choices=SIM_OU_NAO)
    nivelEscolaridade = models.CharField(max_length=2, choices=GRAU_DE_ESCOLARIDADE_CHOICES, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'LGBT - Exame Endocrinologia'



# Cartão SUS
class CartaoSus(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=2, choices=COR_CHOICES)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Cartão SUS - Solicite seu cartão SUS'