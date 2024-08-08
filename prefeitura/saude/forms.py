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
            'horaDaDenuncia': 'Hora da Denúncia',
            'motivoDenuncia': 'Motivo da Denúncia',
            'cidadeDaDenuncia': 'Cidade da Denúncia',
        }

        weight = {
            'horaDaDenuncia': forms.TimeInput(attrs={'type': 'time'}),
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
            'numeroCasa': forms.NumberInput(attrs={'min': 0}),
            'telefone': forms.TextInput(attrs={'pattern': '\(\d{2}\)\s*\d{5}-\d{4}', 'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
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
            'telefone': forms.TextInput(attrs={'pattern': '\(\d{2}\)\s*\d{5}-\d{4}', 'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
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
       
        weight = {
            'cpf': forms.TextInput(attrs={'type': 'number', 'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'type': 'number', 'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Rua, número, bairro'}),
            'pontoReferencia': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Ponto de referência'}),
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
            'cpf': forms.TextInput(attrs={'type': 'number', 'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'type': 'number', 'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Rua, número, bairro'}),
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
            'cpf': forms.TextInput(attrs={'type': 'number', 'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'type': 'number', 'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Rua, número, bairro'}),
            'telefone': forms.TextInput(attrs={'pattern': '\(\d{2}\)\s*\d{5}-\d{4}', 'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
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
            'dataColeta': 'Data da Coleta',
            'dataResultado': 'Data do Resultado',
            'resultado': 'Resultado',
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
            'cpf': forms.TextInput(attrs={'type': 'text', 'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'type': 'text', 'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Rua, número, bairro'}),
            'telefone': forms.TextInput(attrs={'pattern': '\(\d{2}\)\s*\d{5}-\d{4}', 'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'dataColeta': forms.DateInput(attrs={'type': 'date'}),
            'dataResultado': forms.DateInput(attrs={'type': 'date'}),
        }

class GastroenterologistaForm(forms.ModelForm):
    class Meta:
        model = Gastroenterologista
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'nomeRegistro': 'Nome de Registro',
            'cpf': 'CPF',
            'rg': 'RG',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'dataNascimento': 'Data de Nascimento',
            'dataConsulta': 'Data da Consulta',
            'horaConsulta': 'Hora da Consulta',
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
            'cpf': forms.TextInput(attrs={'type': 'number', 'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'type': 'number', 'placeholder': '00.000.000-0'}),
            'endereco': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Rua, número, bairro'}),
            'telefone': forms.TextInput(attrs={'pattern': '\(\d{2}\)\s*\d{5}-\d{4}', 'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'dataConsulta': forms.DateInput(attrs={'type': 'date'}),
            'horaConsulta': forms.TimeInput(attrs={'type': 'time'}),
            'nomeRegistro': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Nome de Registro'}),
            'nome': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Nome'}),
            'cidade': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Cidade'}),
        }

class CartaoSUSForm(forms.ModelForm):
    class Meta:
        model = CartaoSus
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'cor': 'Qual é a sua raça/cor?',
        }