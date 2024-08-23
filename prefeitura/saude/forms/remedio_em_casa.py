from django import forms
from saude.models import RemedioEmCasa, RenovacaoReceita


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
