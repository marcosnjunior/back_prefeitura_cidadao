from django.db import models

# Create your models here.
class Denuncia(models.Model):
    tipo = models.CharField(max_length=100)
    horarioFuncionamento = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    pontoReferencia = models.CharField(max_length=100)
    horaDaDenuncia = models.CharField(max_length=100)
    motivoDenuncia = models.TextField()
    cidadeDaDenuncia = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name = 'Denúncia'

class Vacinacao_Domiciliar(models.Model):
   telefone = models.CharField(max_length=15)
   cep = models.CharField(max_length=100)
   bairro = models.CharField(max_length=100)
   rua = models.CharField(max_length=100)
   numeroCasa = models.IntegerField()
   pontoReferencia = models.CharField(max_length=100)
   dataNascimento = models.DateField()
   
   def __str__(self):
       return self.telefone
   
   class Meta:
        verbose_name = 'Vacinação Domiciliar'
        
class Consulta_Ginecologista_LGBT(models.Model):
    GENERO_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Não-Binário'),
        ('MC', 'Mulher Cis'),
        ('HC', 'Homem Cis'),
        ('MT', 'Mulher Trans'),
        ('HT', 'Homem Trans'),
        ('T', 'Travesti'),
        ('O', 'Outro'),
    ]
    COR_CHOICES=[
        ('B', 'Branco'),
        ('P', 'Preto'),
        ('I', 'Indígena'),
        ('A', 'Amarelo'),
        ('Q', 'Quilombola'),
    ]
    ESTADO_CIVIL_CHOICES=[
        ('S', 'Solteiro'),
        ('C', 'Casado'),
        ('D', 'Divorciado'),
        ('V', 'Viúvo'),
        ('U', 'União Estável'),
    ]
    TIPO_DEFICIENCIA_CHOICES=[
        ('F', 'Física'),
        ('M', 'Mental'),
        ('A', 'Auditiva'),
        ('V', 'Visual'),
        ('O', 'Outra'),
    ]
    TIPO_VIOLENCIA_CHOICES=[
        ('F', 'Física'),
        ('P', 'Psicológica'),
        ('S', 'Sexual'),
        ('M', 'Moral'),
        ('E', 'Econômica'),
        ('O', 'Outra'),
    ]
    MOTIVO_VIOLENCIA_CHOICES=[
        ('S', 'Sexismo'),
        ('L', 'LGBTfobia'),
        ('R', 'Racismo'),
        ('I', 'Intolerância Religiosa'),
        ('X', 'Xenofobia'),
        ('CG', 'Conflito Geracional'),
        ('SR', 'Situação de Rua'),
        ('D', 'Deficiência'),
    ]
    GRAU_DE_PARENTESCO_CHOICES=[
        ('N', 'Não Sofri Violência'),
        ('P', 'Pai'),
        ('M', 'Mãe'),
        ('C', 'Conjuge'),
        ('E', 'Ex-conjuge'),
        ('N', 'Namorado (a)'),
        ('X', 'Ex-namorado (a)'),
        ('A', 'Amigo'),
        ('F', 'Filho'),
        ('I', 'Irmão'),
        ('D', 'Desconhecido'),
        ('O', 'Outro'),
    ]
    LOCAL_DE_VIOLENCIA_CHOICES=[
        ('D', 'Domicílio'),
        ('T', 'Trabalho'),
        ('E', 'Escola'),
        ('R', 'Rua'),
        ('O', 'Outro'),
    ]
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
    possuiDeficiencia = models.BooleanField()
    tipoDeficiencia = models.CharField(max_length=1, choices=TIPO_DEFICIENCIA_CHOICES, blank=True, null=True)
    tipoViolencia = models.CharField(max_length=1, choices=TIPO_VIOLENCIA_CHOICES, blank=True, null=True)
    motivoViolencia = models.CharField(max_length=2, choices=MOTIVO_VIOLENCIA_CHOICES)
    grauParentesco = models.CharField(max_length=1, choices=GRAU_DE_PARENTESCO_CHOICES)
    localViolencia = models.CharField(max_length=1, choices=LOCAL_DE_VIOLENCIA_CHOICES)
    tenativadeSuicidio = models.BooleanField()
    cpf = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    def __str__(self):
           return self.nomeSocial
    class Meta:
        verbose_name = 'Consulta Ginecologista LGBT'

class RemedioEmCasa(models.Model):
    PAICENTE_ACAMADO_CHOICES = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    nome = models.CharField(max_length=100)
    numeroCNS = models.CharField(max_length=100)
    unidadeSaude = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    estadoUF = models.CharField(max_length=2)
    cep = models.CharField(max_length=100)
    pacienteAcamado = models.CharField(max_length=1, choices=PAICENTE_ACAMADO_CHOICES)
    dataNascimento = models.DateField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Remédio em Casa'

class RenovacaoReceita(models.Model):
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    pontoReferencia = models.CharField(max_length=100)

class SoliciteSuaCirugia(models.Model):
    EXAME_CHOICES = [
        ('E', 'Ecocardiograma'),
        ('R', 'Ressonância Magnética'),
        ('T', 'Tomografia Computadorizada'),
        ('U', 'Ultrassonografia'),
        ('M', 'Mamografia'),
        ('P', 'Papanicolau'),
        ('H', 'Hemograma'),
        ('G', 'Glicemia'),
    ]
    nome = models.CharField(max_length=100)
    sus = models.CharField(max_length=100)
    tipoExame = models.CharField(max_length=2, choices=EXAME_CHOICES)
    informacoesAdicionais = models.TextField()


class Exames(models.Model):
    EXAME_CHOICES = [
        ('E', 'Ecocardiograma'),
        ('R', 'Ressonância Magnética'),
        ('T', 'Tomografia Computadorizada'),
        ('U', 'Ultrassonografia'),
        ('M', 'Mamografia'),
        ('P', 'Papanicolau'),
        ('H', 'Hemograma'),
        ('G', 'Glicemia'),
    ]
    nome = models.CharField(max_length=100)
    sus = models.CharField(max_length=100)
    tipoExame = models.CharField(max_length=2, choices=EXAME_CHOICES)
    informacoesAdicionais = models.TextField()
    telefone = models.CharField(max_length=15)

class Gastroenterologista(models.Model):
    GENERO_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Não-Binário'),
        ('MC', 'Mulher Cis'),
        ('HC', 'Homem Cis'),
        ('MT', 'Mulher Trans'),
        ('HT', 'Homem Trans'),
        ('T', 'Travesti'),
        ('O', 'Outro'),
    ]

    COR_CHOICE = [
        ('B', 'Branco'),
        ('P', 'Preto'),
        ('I', 'Indígena'),
        ('A', 'Amarelo'),
        ('Q', 'Quilombola'),
    ]
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Solteiro'),
        ('C', 'Casado'),
        ('D', 'Divorciado'),
        ('V', 'Viúvo'),
        ('U', 'União Estável'),
    ]
    nome = models.CharField(max_length=100)
    nomeRegistro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    identidadeGenero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    orientacaoSexual = models.CharField(max_length=2, choices=GENERO_CHOICES)
    cor = models.CharField(max_length=2, choices=COR_CHOICE)
    estadoCivil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES)
    possuiDeficiencia = models.BooleanField()
    dataNascimento = models.DateField()
    cpf = models.CharField(max_length=100)
  
    def __str__(self):
        return self.nome

class ExameCitopatologico(models.Model):
    GENERO_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Não-Binário'),
        ('MC', 'Mulher Cis'),
        ('HC', 'Homem Cis'),
        ('MT', 'Mulher Trans'),
        ('HT', 'Homem Trans'),
        ('T', 'Travesti'),
        ('O', 'Outro'),
    ]

    COR_CHOICE = [
        ('B', 'Branco'),
        ('P', 'Preto'),
        ('I', 'Indígena'),
        ('A', 'Amarelo'),
        ('Q', 'Quilombola'),
    ]
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Solteiro'),
        ('C', 'Casado'),
        ('D', 'Divorciado'),
        ('V', 'Viúvo'),
        ('U', 'União Estável'),
    ]
    LOCAL_DE_VIOLENCIA_CHOICES=[
        ('D', 'Domicílio'),
        ('T', 'Trabalho'),
        ('E', 'Escola'),
        ('R', 'Rua'),
        ('O', 'Outro'),
    ]
    SIM_OU_NAO = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    nome = models.CharField(max_length=100)
    nomeRegistro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    identidadeGenero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    orientacaoSexual = models.CharField(max_length=2, choices=GENERO_CHOICES)
    cor = models.CharField(max_length=2, choices=COR_CHOICE)
    estadoCivil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES)
    localViolencia = models.CharField(max_length=1, choices=LOCAL_DE_VIOLENCIA_CHOICES)
    cpf = models.CharField(max_length=100)
    tipoDeficiencia = models.CharField(max_length=100)
    recebeBeneficio = models.BooleanField()
    pensamentoSuicida = models.CharField(max_length=1, choices=SIM_OU_NAO)
    tentativaSuicidio = models.CharField(max_length=1, choices=SIM_OU_NAO)
    
