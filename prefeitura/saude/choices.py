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

SIM_OU_NAO = [
    ('S', 'Sim'),
    ('N', 'Não'),
]

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

GRAU_DE_ESCOLARIDADE_CHOICES = [
    ('A', 'Analfabeto'),
    ('F', 'Fundamental'),
    ('M', 'Médio'),
    ('S', 'Superior'),
    ('P', 'Pós-Graduação'),
]

SITUACAO_TRABALHANDO_CHOICES = [
    ('E', 'Empregado'),
    ('D', 'Desempregado'),
    ('A', 'Aposentado'),
    ('E', 'Empreendedor'),
]

RECEBE_TIPO_BENEFICIO_CHOICES = [
    ('B', 'Bolsa Família'),
    ('A', 'Aposentadoria'),
    ('S', 'Seguro Desemprego'),
    ('O', 'Outro'),
    ('U', 'Bolsa Universidade'),
]

ESTADO_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]