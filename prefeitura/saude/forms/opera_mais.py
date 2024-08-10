from django import forms
from saude.models import SoliciteSuaCirugia, Exames

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