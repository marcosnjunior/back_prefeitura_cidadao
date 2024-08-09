from django import forms

from .models import *

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'
        labels = {
            'tipo': 'Tipo de Estabelecimento',
            'horarioFuncionamento': 'Horário de Funcionamento',
            'endereco': 'Endereço',
            'bairro': 'Bairro',
            'pontoReferencia': 'Ponto de Referência',
            'motivoDenuncia': 'Motivo da Denúncia',
            'cidadeDaDenuncia': 'Cidade da Denúncia',
            'horaDaDenuncia': 'Hora da Denúncia',
        }

        widgets = {
            'tipo': forms.TextInput(attrs={'placeholder': 'Tipo de Estabelecimento'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Endereço'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'motivoDenuncia': forms.Textarea(attrs={'placeholder': 'Motivo da Denúncia'}),
            'cidadeDaDenuncia': forms.TextInput(attrs={'placeholder': 'Cidade da Denúncia'}),
            'horarioFuncionamento': forms.TextInput(attrs={'type': 'time', 'placeholder': '00:00'}),
            'horaDaDenuncia': forms.TextInput(attrs={'type': 'time', 'placeholder': '00:00'}),
            'pontoReferencia': forms.TextInput(attrs={'placeholder': 'Ponto de Referência'}),
        }
        
class VacinacaoDomiciliarForm(forms.ModelForm):
    class Meta:
        model = Vacinacao_Domiciliar
        fields = '__all__'
        labels = {
            'telefone': 'Telefone',
            'cep': 'CEP',
            'bairro': 'Bairro',
            'rua': 'Rua',
            'numeroCasa': 'Número da Casa',
            'pontoReferencia': 'Ponto de Referência',
            'dataNascimento': 'Data de Nascimento',
        }

        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': '00000-000', 'pattern': '\d{5}-\d{3}'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'rua': forms.TextInput(attrs={'placeholder': 'Rua'}),
            'pontoReferencia': forms.TextInput(attrs={'placeholder': 'Ponto de Referência'}),
            'numeroCasa': forms.NumberInput(attrs={'min': 0}),
            'telefone': forms.TextInput(attrs={'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
        }
        
class ConsultaGinecologistaLGBTForm(forms.ModelForm):
    class Meta:
        model = Consulta_Ginecologista_LGBT
        fields = '__all__'
        labels = {
            'nomeSocial': 'Nome social',
            'nomeRegistro': 'Nome de Registro',
            'dataNascimento': 'Data de Nascimento',
            'orientacaoSexual': 'Orientação Sexual',
            'identidadeGenero': 'Gênero de Identidade',
            'estadoCivil': 'Estado Civil',
            'email': 'E-mail',
            'tipoViolencia': 'Qual é o tipo de violência?',
            'possuiDeficiencia': 'Você possui alguma deficiência?',
            'tipoDeficiencia': 'Qual tipo de deficiência?',
            'tenativadeSuicidio': 'Você já tentou suicídio?',
            'motivoViolencia': 'Qual o motivo da violência?',
            'cidadeOneReside': 'Qual cidade você reside?',
            'endereco': 'Endereço',
            'grauParentesco': 'Qual o grau de parentesco do agressor?',
            'localViolencia': 'Onde ocorreu a violência?',
        }

        widgets = {
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
        }


class RemedioEmCasaForm(forms.ModelForm):
    class Meta:
        model = RemedioEmCasa
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'numeroCNS': 'Número do CNS',
            'unidadeSaude': 'Unidade de Saúde',
            'endereco': 'Endereço',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'cidade': 'Cidade',
            'telefone': 'Telefone',
            'estadoUF': 'Estado',
            'pacienteAcamado': 'Paciente acamado?',
            'dataNascimento': 'Data de Nascimento',
        }

        widgets = {
            'telefone': forms.TextInput(attrs={'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
            'cep': forms.TextInput(attrs={'placeholder': '00000-000', 'pattern': '\d{5}-\d{3}'}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'numeroCNS': forms.NumberInput(attrs={'placeholder': '000000000000000'}),
            'nome': forms.TextInput(attrs={'placeholder': 'Nome Completo'}),
            'unidadeSaude': forms.TextInput(attrs={'placeholder': 'Unidade de Saúde'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade'}),
        }

class RenovacaoReceitaForm(forms.ModelForm):
    class Meta:
        model = RenovacaoReceita
        fields = '__all__'
       
        labels = {
            'cpf': 'CPF',
            'rg': 'RG',
            'endereco': 'Endereço',
            'pontoReferencia': 'Ponto de Referência',
        }
       
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00', 'pattern': '\d{3}\.\d{3}\.\d{3}-\d{2}'}),
            'rg': forms.TextInput(attrs={'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}),
            'pontoReferencia': forms.TextInput(attrs={'placeholder': 'Ponto de referência'}),
        }

class SoliciteCirurgiaForm(forms.ModelForm):
    class Meta:
        model = SoliciteSuaCirugia
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'rg': 'RG',
            'endereco': 'Endereço',
            'tipoCirurgia': 'Tipo de Cirurgia',
        }
       
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}),
        }

class ExamesForm(forms.ModelForm):
    class Meta:
        model = Exames
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'rg': 'RG',
            'endereco': 'Endereço',
            'tipoExame': 'Tipo de Exame',
            'informacoesAdicionais': 'Informações Adicionais',
        }
      
        widgets = {
            'informacoesAdicionais': forms.Textarea(attrs={'placeholder': 'Informações adicionais'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
        }

class ExameCitopatologicoForm(forms.ModelForm):
    class Meta:
        model = ExameCitopatologico
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'nomeRegistro': 'Nome de Registro',
            'cpf': 'CPF',
            'rg': 'RG',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'dataNascimento': 'Data de Nascimento',
            'recebeBeneficio': 'Recebe algum benefício?',
            'tipoDeficiencia': 'Qual tipo de deficiência?',
            'pensamentoSuicida': 'Já teve pensamento suicida?',
            'tentativaSuicidio': 'Já tentou suicídio?',
            'localViolencia': 'Onde ocorreu a violência?',
            'estadoCivil': 'Qual é o seu estado civil?',
            'orientacaoSexual': 'Qual é a sua orientação sexual?',
            'identidadeGenero': 'Por qual gênero você se identifica?',
        }
      
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class GastroenterologistaForm(forms.ModelForm):
    class Meta:
        model = Gastroenterologista
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'nomeRegistro': 'Nome de Registro',
            'cpf': 'CPF',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'dataNascimento': 'Data de Nascimento',
            'motivoConsulta': 'Motivo da Consulta',
            'possuiDeficiencia': 'Possui alguma deficiência?',
            'tipoDeficiencia': 'Qual tipo de deficiência?',
            'nivelEscolaridade': 'Qual é o seu nível de escolaridade?',
            'trabalhoSituacao': 'Qual é a sua situação de trabalho?',
            'orientacaoSexual': 'Qual é a sua orientação sexual?',
            'identidadeGenero': 'Por qual gênero você se identifica?',
            'estadoCivil': 'Qual é o seu estado civil?',
        }
      
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome Completo'}),
            'nomeRegistro': forms.TextInput(attrs={'placeholder': 'Nome de Registro'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
        }

class CartaoSUSForm(forms.ModelForm):
    class Meta:
        model = CartaoSus
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'cor': 'Qual é a sua raça/cor?',
        }


class ExameEndocrinologiaForm(forms.ModelForm):
    class Meta:
        model = ExameEndocrinologia
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'nomeRegistro': 'Nome de Registro',
            'cpf': 'CPF',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'dataNascimento': 'Data de Nascimento',
            'motivoConsulta': 'Motivo da Consulta',
            'possuiDeficiencia': 'Possui alguma deficiência?',
            'tipoDeficiencia': 'Qual tipo de deficiência?',
            'nivelEscolaridade': 'Qual é o seu nível de escolaridade?',
            'trabalhoSituacao': 'Qual é a sua situação de trabalho?',
            'orientacaoSexual': 'Qual é a sua orientação sexual?',
            'identidadeGenero': 'Por qual gênero você se identifica?',
            'estadoCivil': 'Qual é o seu estado civil?',
            'recebeBeneficio': 'Recebe algum benefício?',
            'pensamentoSuicida': 'Já teve pensamento suicida?',
            'tentativaSuicidio': 'Já tentou suicídio?',
            'localViolencia': 'Onde ocorreu a violência?',
            'temDeficiencia': 'Possui alguma deficiência?',
        }
      
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome Completo'}),
            'nomeRegistro': forms.TextInput(attrs={'placeholder': 'Nome de Registro'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
        }