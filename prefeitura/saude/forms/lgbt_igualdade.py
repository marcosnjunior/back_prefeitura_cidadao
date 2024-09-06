from django import forms
from saude.models import Consulta_Ginecologista_LGBT, ExameCitopatologico, Gastroenterologista, ExameEndocrinologia

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
            'status': forms.TextInput(attrs={'type': 'hidden'}),
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
            'status': forms.TextInput(attrs={'type': 'hidden'}),
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
            'status': forms.TextInput(attrs={'type': 'hidden'}),
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
            'status': forms.TextInput(attrs={'type': 'hidden'}),
        }